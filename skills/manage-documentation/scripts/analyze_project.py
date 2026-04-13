#!/usr/bin/env python3
"""
Main project analysis script for extracting service information from source code.
Analyzes the codebase to extract language, dependencies, configuration, and structure.
"""

import json
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class ProjectAnalysis:
    """Data class for holding project analysis results"""
    service_name: str
    language: str
    language_version: Optional[str]
    dependencies: Dict[str, str]
    environment_variables: Dict[str, Dict[str, str]]
    databases: List[str]
    message_broker: Optional[str]
    frameworks: List[str]
    api_type: Optional[str]  # REST, GraphQL, gRPC, etc.


class ProjectAnalyzer:
    """Analyzes a project directory to extract service information"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.analysis = None
        self._dependencies_cache = None

    def analyze(self) -> Dict[str, Any]:
        """Run complete analysis of the project"""
        results = {
            "service_name": self.extract_service_name(),
            "language": self.detect_language(),
            "language_version": self.extract_language_version(),
            "dependencies": self.extract_dependencies(),
            "environment_variables": self.extract_environment_variables(),
            "databases": self.detect_databases(),
            "message_broker": self.detect_message_broker(),
            "frameworks": self.detect_frameworks(),
            "api_type": self.detect_api_type(),
            "main_files": self.find_main_files(),
            "project_structure": self.analyze_project_structure(),
        }
        return results

    def extract_service_name(self) -> str:
        """Extract service name from package.json, setup.py, or pom.xml"""
        # Check package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                data = json.loads(package_json.read_text())
                return data.get("name", "unknown-service")
            except:
                pass

        # Check setup.py
        setup_py = self.project_root / "setup.py"
        if setup_py.exists():
            try:
                content = setup_py.read_text()
                match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1)
            except:
                pass

        # Check pom.xml
        pom_xml = self.project_root / "pom.xml"
        if pom_xml.exists():
            try:
                content = pom_xml.read_text()
                match = re.search(r'<artifactId>([^<]+)</artifactId>', content)
                if match:
                    return match.group(1)
            except:
                pass

        # Fallback to directory name
        return self.project_root.name

    def detect_language(self) -> str:
        """Detect primary programming language"""
        file_counts = {}

        for py_file in self.project_root.rglob("*.py"):
            if "venv" not in py_file.parts and "__pycache__" not in py_file.parts:
                file_counts["Python"] = file_counts.get("Python", 0) + 1

        for js_file in self.project_root.rglob("*.js"):
            if "node_modules" not in js_file.parts:
                file_counts["JavaScript"] = file_counts.get("JavaScript", 0) + 1

        for ts_file in self.project_root.rglob("*.ts"):
            if "node_modules" not in ts_file.parts:
                file_counts["TypeScript"] = file_counts.get("TypeScript", 0) + 1

        for java_file in self.project_root.rglob("*.java"):
            file_counts["Java"] = file_counts.get("Java", 0) + 1

        # Check manifest files
        if (self.project_root / "package.json").exists():
            return "JavaScript/Node.js"
        if (self.project_root / "setup.py").exists():
            return "Python"
        if (self.project_root / "pom.xml").exists():
            return "Java"

        if file_counts:
            return max(file_counts, key=file_counts.get)

        return "Unknown"

    def extract_language_version(self) -> Optional[str]:
        """Extract language version"""
        # Check Node.js version in package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                data = json.loads(package_json.read_text())
                engines = data.get("engines", {})
                return engines.get("node")
            except:
                pass

        # Check Python version in setup.py
        setup_py = self.project_root / "setup.py"
        if setup_py.exists():
            try:
                content = setup_py.read_text()
                match = re.search(r'python_requires\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1)
            except:
                pass

        return None

    def extract_dependencies(self) -> Dict[str, str]:
        """Extract dependencies from package.json, requirements.txt, pom.xml, etc."""
        if self._dependencies_cache is not None:
            return dict(self._dependencies_cache)

        dependencies = {}

        # Node.js dependencies
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                data = json.loads(package_json.read_text())
                dependencies.update(data.get("dependencies", {}))
                dependencies.update(data.get("devDependencies", {}))
            except:
                pass

        # Python dependencies
        requirements_txt = self.project_root / "requirements.txt"
        if requirements_txt.exists():
            try:
                for line in requirements_txt.read_text().strip().split("\n"):
                    if "==" in line:
                        name, version = line.split("==")
                        dependencies[name.strip()] = version.strip()
                    elif line.strip() and not line.startswith("#"):
                        dependencies[line.strip()] = "unknown"
            except:
                pass

        # Java dependencies in pom.xml
        pom_xml = self.project_root / "pom.xml"
        if pom_xml.exists():
            try:
                content = pom_xml.read_text()
                # Simple regex extraction, not a full XML parser
                for match in re.finditer(
                    r'<artifactId>([^<]+)</artifactId>\s*</dependency>\s*.*?<version>([^<]+)</version>',
                    content,
                    re.DOTALL,
                ):
                    dependencies[match.group(1)] = match.group(2)
            except:
                pass

        self._dependencies_cache = dict(dependencies)
        return dict(self._dependencies_cache)

    def extract_environment_variables(self) -> Dict[str, Dict[str, str]]:
        """Extract environment variables from .env, config files, and code"""
        env_vars = {}

        # Check .env files
        for env_file in [".env", ".env.example", ".env.default"]:
            env_path = self.project_root / env_file
            if env_path.exists():
                try:
                    for line in env_path.read_text().strip().split("\n"):
                        if "=" in line and not line.startswith("#"):
                            key, value = line.split("=", 1)
                            key = key.strip()
                            value = value.strip()
                            env_vars[key] = {
                                "default": value if value else "none",
                                "source": env_file,
                            }
                except:
                    pass

        return env_vars

    def detect_databases(self) -> List[str]:
        """Detect database types used by the service"""
        databases = set()

        # Check for common database imports/dependencies
        deps = self.extract_dependencies()
        db_keywords = {
            "PostgreSQL": ["postgres", "pg", "psycopg2"],
            "MongoDB": ["mongodb", "mongoose", "pymongo"],
            "MySQL": ["mysql", "mysql2", "pymysql"],
            "SQLite": ["sqlite", "sqlite3"],
            "Redis": ["redis"],
            "Cassandra": ["cassandra"],
            "Neo4j": ["neo4j"],
            "DynamoDB": ["dynamodb", "boto3"],
        }

        for db, keywords in db_keywords.items():
            for keyword in keywords:
                if keyword.lower() in [dep.lower() for dep in deps.keys()]:
                    databases.add(db)
                    break

        # Check for connection files
        for root, dirs, files in os.walk(self.project_root):
            if ".git" in root or "node_modules" in root or "venv" in root:
                continue
            for file in files:
                if any(x in file.lower() for x in ["database", "db.config", "mongo"]):
                    filepath = os.path.join(root, file)
                    try:
                        content = open(filepath, "r", errors="ignore").read()
                        if "mongodb" in content.lower():
                            databases.add("MongoDB")
                        elif "postgres" in content.lower():
                            databases.add("PostgreSQL")
                    except:
                        pass

        return list(databases)

    def detect_message_broker(self) -> Optional[str]:
        """Detect message broker type (MQTT, RabbitMQ, Kafka, etc.)"""
        deps = self.extract_dependencies()
        dep_lower = {dep.lower(): dep for dep in deps.keys()}

        # Check for MQTT
        if any(key in dep_lower for key in ["mqtt", "paho-mqtt", "mqtt.js"]):
            return "MQTT"

        # Check for RabbitMQ
        if any(
            key in dep_lower
            for key in ["amqp", "pika", "rabbitmq", "nats", "node-amqp"]
        ):
            return "RabbitMQ/AMQP"

        # Check for Kafka
        if any(
            key in dep_lower
            for key in ["kafka", "kafka-python", "kafkajs", "confluent-kafka"]
        ):
            return "Apache Kafka"

        return None

    def detect_frameworks(self) -> List[str]:
        """Detect frameworks used"""
        frameworks = []
        deps = self.extract_dependencies()
        dep_lower = {dep.lower(): dep for dep in deps.keys()}

        framework_mappings = {
            "Express": ["express"],
            "FastAPI": ["fastapi"],
            "Flask": ["flask"],
            "Django": ["django"],
            "NestJS": ["@nestjs"],
            "Spring": ["spring-boot", "springframework"],
            "React": ["react"],
            "Vue": ["vue"],
            "Angular": ["@angular"],
        }

        for framework, keywords in framework_mappings.items():
            for keyword in keywords:
                if keyword.lower() in dep_lower:
                    frameworks.append(framework)
                    break

        return frameworks

    def detect_api_type(self) -> Optional[str]:
        """Detect API type (REST, GraphQL, gRPC, etc.)"""
        deps = self.extract_dependencies()
        dep_names = {dep.lower() for dep in deps.keys()}

        if any(key in dep_names for key in ["graphql", "apollo", "@graphql"]):
            return "GraphQL"
        if any(key in dep_names for key in ["grpc", "protobuf"]):
            return "gRPC"

        rest_indicators = {
            "express",
            "fastapi",
            "flask",
            "django",
            "@nestjs/core",
            "@nestjs/common",
            "spring-boot-starter-web",
            "spring-web",
        }
        if dep_names.intersection(rest_indicators):
            return "REST"

        return None

    def find_main_files(self) -> List[str]:
        """Find main entry point files"""
        main_files = []

        # Check package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                data = json.loads(package_json.read_text())
                if "main" in data:
                    main_files.append(data["main"])
            except:
                pass

        # Check for common entry points
        for entry in ["index.js", "index.ts", "main.py", "app.py", "server.js", "src/index.js", "src/index.ts"]:
            path = self.project_root / entry
            if path.exists():
                main_files.append(entry)

        return main_files

    def analyze_project_structure(self) -> Dict[str, List[str]]:
        """Analyze project directory structure"""
        structure = {"directories": [], "key_files": []}

        top_level_dirs = []
        top_level_files = []

        try:
            for item in self.project_root.iterdir():
                if item.name.startswith("."):
                    continue
                if item.is_dir():
                    if item.name not in ["node_modules", "venv", ".git", "dist", "build"]:
                        top_level_dirs.append(item.name)
                else:
                    if item.name in [
                        "package.json",
                        "setup.py",
                        "requirements.txt",
                        "Dockerfile",
                        "docker-compose.yml",
                        "README.md",
                        ".env",
                        "pom.xml",
                    ]:
                        top_level_files.append(item.name)
        except:
            pass

        structure["directories"] = sorted(top_level_dirs)
        structure["key_files"] = sorted(top_level_files)

        return structure


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python analyze_project.py <project_root>")
        sys.exit(1)

    project_root = sys.argv[1]

    if not os.path.isdir(project_root):
        print(f"Error: {project_root} is not a directory")
        sys.exit(1)

    analyzer = ProjectAnalyzer(project_root)
    results = analyzer.analyze()

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
