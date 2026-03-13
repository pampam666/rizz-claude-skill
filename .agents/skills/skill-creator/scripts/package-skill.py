#!/usr/bin/env python3
"""
Skill Packager Script

Packages a Cline Skill directory into a shareable .skill archive format.
Creates a compressed archive with manifest for easy distribution and installation.

Usage:
    python package-skill.py <skill_directory> [output_directory]

Example:
    python package-skill.py ./my-skill ./packaged-skills/
"""

import os
import sys
import json
import shutil
import zipfile
import yaml
from pathlib import Path
from datetime import datetime


def parse_yaml_frontmatter(file_path: str) -> dict:
    """
    Parse YAML frontmatter from a SKILL.md file.
    
    Args:
        file_path: Path to the SKILL.md file
        
    Returns:
        Dictionary containing frontmatter metadata
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter between --- markers
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            try:
                return yaml.safe_load(frontmatter_text)
            except yaml.YAMLError as e:
                print(f"Error parsing YAML frontmatter: {e}")
                return {}
    
    return {}


def validate_skill_directory(skill_dir: str) -> tuple[bool, list[str]]:
    """
    Validate a skill directory structure.
    
    Args:
        skill_dir: Path to the skill directory
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    skill_path = Path(skill_dir)
    
    # Check directory exists
    if not skill_path.exists():
        errors.append(f"Directory does not exist: {skill_dir}")
        return False, errors
    
    # Check for SKILL.md
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing required file: SKILL.md")
        return False, errors
    
    # Validate frontmatter
    frontmatter = parse_yaml_frontmatter(str(skill_md))
    
    if 'name' not in frontmatter:
        errors.append("SKILL.md missing required 'name' field in frontmatter")
    
    if 'description' not in frontmatter:
        errors.append("SKILL.md missing required 'description' field in frontmatter")
    
    # Check naming convention (kebab-case)
    dir_name = skill_path.name
    if not dir_name.islower() or ' ' in dir_name:
        errors.append(f"Directory name '{dir_name}' should use kebab-case (lowercase, no spaces)")
    
    if frontmatter.get('name') and ' ' in frontmatter.get('name', ''):
        errors.append(f"Skill name '{frontmatter['name']}' should use kebab-case (no spaces)")
    
    return len(errors) == 0, errors


def create_manifest(skill_dir: str, frontmatter: dict) -> dict:
    """
    Create a manifest for the skill package.
    
    Args:
        skill_dir: Path to the skill directory
        frontmatter: Parsed frontmatter from SKILL.md
        
    Returns:
        Manifest dictionary
    """
    skill_path = Path(skill_dir)
    
    # Collect all files
    files = []
    for root, _, filenames in os.walk(skill_dir):
        for filename in filenames:
            file_path = Path(root) / filename
            rel_path = file_path.relative_to(skill_path)
            files.append(str(rel_path))
    
    manifest = {
        "name": frontmatter.get('name', skill_path.name),
        "description": frontmatter.get('description', ''),
        "version": frontmatter.get('version', '1.0.0'),
        "author": frontmatter.get('author', 'Unknown'),
        "tags": frontmatter.get('tags', []),
        "created": datetime.now().isoformat(),
        "files": files,
        "skill_format_version": "1.0"
    }
    
    return manifest


def package_skill(skill_dir: str, output_dir: str = None) -> str:
    """
    Package a skill directory into a .skill archive.
    
    Args:
        skill_dir: Path to the skill directory
        output_dir: Output directory for the package (default: same as skill_dir)
        
    Returns:
        Path to the created package
    """
    skill_path = Path(skill_dir).resolve()
    
    # Validate skill directory
    is_valid, errors = validate_skill_directory(skill_dir)
    if not is_valid:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    
    print(f"✓ Skill directory validated: {skill_dir}")
    
    # Parse frontmatter
    skill_md = skill_path / "SKILL.md"
    frontmatter = parse_yaml_frontmatter(str(skill_md))
    skill_name = frontmatter.get('name', skill_path.name)
    
    # Determine output location
    if output_dir:
        output_path = Path(output_dir).resolve()
    else:
        output_path = skill_path.parent
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create package filename
    package_name = f"{skill_name.replace(' ', '-').lower()}.skill"
    package_path = output_path / package_name
    
    # Create manifest
    manifest = create_manifest(skill_dir, frontmatter)
    
    # Create the archive
    with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add manifest
        zf.writestr('manifest.json', json.dumps(manifest, indent=2))
        
        # Add all skill files
        for root, _, filenames in os.walk(skill_dir):
            for filename in filenames:
                file_path = Path(root) / filename
                arcname = file_path.relative_to(skill_path)
                zf.write(file_path, arcname)
    
    print(f"✓ Package created: {package_path}")
    print(f"  - Skill name: {skill_name}")
    print(f"  - Version: {manifest['version']}")
    print(f"  - Files: {len(manifest['files'])}")
    
    return str(package_path)


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nError: Missing required argument <skill_directory>")
        sys.exit(1)
    
    skill_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        package_skill(skill_dir, output_dir)
    except Exception as e:
        print(f"Error packaging skill: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()