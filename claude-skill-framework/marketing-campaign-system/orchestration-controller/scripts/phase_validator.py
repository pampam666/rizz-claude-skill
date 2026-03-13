#!/usr/bin/env python3
"""
Phase Validator Script

Validates checkpoint criteria between workflow phases.
Ensures quality gates are met before proceeding to next phase.

Usage:
    python phase_validator.py <workflow_state.json> <phase_name>

Example:
    python phase_validator.py workflow_state.json brand_extraction
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Tuple


# Checkpoint thresholds for each phase
CHECKPOINT_THRESHOLDS = {
    "initialization": {
        "required_fields": ["workflow_id", "company_url", "campaign_parameters"],
        "min_confidence": 0.0
    },
    "brand_extraction": {
        "required_fields": ["brand_dna"],
        "min_confidence": 0.7,
        "required_brand_fields": ["company_name", "tone_attributes", "positioning"]
    },
    "market_research": {
        "required_fields": ["research_artifacts"],
        "min_artifacts": 10,
        "required_artifact_types": ["market_size", "competitors", "trends"]
    },
    "campaign_strategy": {
        "required_fields": ["strategy_artifacts"],
        "min_strategies": 11,
        "required_strategy_types": ["positioning", "messaging", "channel_strategy"]
    },
    "research_writing": {
        "required_fields": ["deliverables.research_document_path"],
        "file_must_exist": True
    },
    "campaign_planning": {
        "required_fields": ["deliverables.campaign_plan_path"],
        "file_must_exist": True
    },
    "article_execution": {
        "required_fields": ["deliverables.article_paths"],
        "min_articles": None,  # Dynamic based on campaign_parameters.article_count
    },
    "quality_assurance": {
        "required_fields": ["quality_reports"],
        "all_must_pass": True
    }
}


def load_workflow_state(state_path: str) -> Dict[str, Any]:
    """Load workflow state from JSON file."""
    path = Path(state_path)
    if not path.exists():
        raise FileNotFoundError(f"Workflow state file not found: {state_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_nested_value(data: Dict, path: str) -> Any:
    """Get nested dictionary value using dot notation."""
    keys = path.split('.')
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value


def validate_initialization(state: Dict) -> Tuple[bool, float, str]:
    """Validate initialization phase."""
    threshold = CHECKPOINT_THRESHOLDS["initialization"]
    missing_fields = []
    
    for field in threshold["required_fields"]:
        if field not in state or not state[field]:
            missing_fields.append(field)
    
    if missing_fields:
        return False, 0.0, f"Missing required fields: {missing_fields}"
    
    # Validate URL format
    url = state.get("company_url", "")
    if not url.startswith(("http://", "https://")):
        return False, 0.0, "Invalid URL format. Must start with http:// or https://"
    
    return True, 1.0, "Initialization validated successfully"


def validate_brand_extraction(state: Dict) -> Tuple[bool, float, str]:
    """Validate brand DNA extraction phase."""
    threshold = CHECKPOINT_THRESHOLDS["brand_extraction"]
    
    # Check brand_dna exists
    brand_dna = state.get("brand_dna", {})
    if not brand_dna:
        return False, 0.0, "brand_dna object is empty or missing"
    
    # Check required brand fields
    missing_fields = []
    for field in threshold["required_brand_fields"]:
        if field not in brand_dna:
            missing_fields.append(field)
    
    if missing_fields:
        return False, 0.0, f"Missing brand DNA fields: {missing_fields}"
    
    # Calculate confidence score
    confidence = brand_dna.get("confidence_score", 0)
    
    if confidence < threshold["min_confidence"]:
        return False, confidence, f"Confidence score {confidence} below threshold {threshold['min_confidence']}"
    
    return True, confidence, f"Brand DNA extracted with confidence: {confidence:.2f}"


def validate_market_research(state: Dict) -> Tuple[bool, float, str]:
    """Validate market research phase."""
    threshold = CHECKPOINT_THRESHOLDS["market_research"]
    
    research_artifacts = state.get("research_artifacts", {})
    if not research_artifacts:
        return False, 0.0, "research_artifacts object is empty or missing"
    
    # Count artifacts
    artifact_count = len(research_artifacts.keys())
    
    # Check for required artifact types
    missing_types = []
    for artifact_type in threshold["required_artifact_types"]:
        if artifact_type not in research_artifacts:
            missing_types.append(artifact_type)
    
    if missing_types:
        return False, artifact_count / threshold["min_artifacts"], \
               f"Missing artifact types: {missing_types}"
    
    if artifact_count < threshold["min_artifacts"]:
        return False, artifact_count / threshold["min_artifacts"], \
               f"Only {artifact_count} artifacts, need at least {threshold['min_artifacts']}"
    
    confidence = min(1.0, artifact_count / threshold["min_artifacts"])
    return True, confidence, f"Market research complete with {artifact_count} artifacts"


def validate_campaign_strategy(state: Dict) -> Tuple[bool, float, str]:
    """Validate campaign strategy phase."""
    threshold = CHECKPOINT_THRESHOLDS["campaign_strategy"]
    
    strategy_artifacts = state.get("strategy_artifacts", {})
    if not strategy_artifacts:
        return False, 0.0, "strategy_artifacts object is empty or missing"
    
    # Count strategies
    strategy_count = len(strategy_artifacts.keys())
    
    # Check for required strategy types
    missing_types = []
    for strategy_type in threshold["required_strategy_types"]:
        if strategy_type not in strategy_artifacts:
            missing_types.append(strategy_type)
    
    if missing_types:
        return False, strategy_count / threshold["min_strategies"], \
               f"Missing strategy types: {missing_types}"
    
    if strategy_count < threshold["min_strategies"]:
        return False, strategy_count / threshold["min_strategies"], \
               f"Only {strategy_count} strategies, need at least {threshold['min_strategies']}"
    
    confidence = min(1.0, strategy_count / threshold["min_strategies"])
    return True, confidence, f"Campaign strategy complete with {strategy_count} strategies"


def validate_research_writing(state: Dict) -> Tuple[bool, float, str]:
    """Validate research document creation phase."""
    threshold = CHECKPOINT_THRESHOLDS["research_writing"]
    
    doc_path = state.get("deliverables", {}).get("research_document_path", "")
    
    if not doc_path:
        return False, 0.0, "Research document path not set"
    
    if threshold["file_must_exist"]:
        if not Path(doc_path).exists():
            return False, 0.0, f"Research document not found at: {doc_path}"
    
    return True, 1.0, f"Research document created: {doc_path}"


def validate_campaign_planning(state: Dict) -> Tuple[bool, float, str]:
    """Validate campaign plan creation phase."""
    threshold = CHECKPOINT_THRESHOLDS["campaign_planning"]
    
    plan_path = state.get("deliverables", {}).get("campaign_plan_path", "")
    
    if not plan_path:
        return False, 0.0, "Campaign plan path not set"
    
    if threshold["file_must_exist"]:
        if not Path(plan_path).exists():
            return False, 0.0, f"Campaign plan not found at: {plan_path}"
    
    return True, 1.0, f"Campaign plan created: {plan_path}"


def validate_article_execution(state: Dict) -> Tuple[bool, float, str]:
    """Validate article content execution phase."""
    threshold = CHECKPOINT_THRESHOLDS["article_execution"]
    
    # Get requested article count
    requested_count = state.get("campaign_parameters", {}).get("article_count", 10)
    
    article_paths = state.get("deliverables", {}).get("article_paths", [])
    actual_count = len(article_paths)
    
    if actual_count < requested_count:
        confidence = actual_count / requested_count if requested_count > 0 else 0
        return False, confidence, \
               f"Only {actual_count}/{requested_count} articles generated"
    
    return True, 1.0, f"All {actual_count} articles generated successfully"


def validate_quality_assurance(state: Dict) -> Tuple[bool, float, str]:
    """Validate quality assurance phase."""
    threshold = CHECKPOINT_THRESHOLDS["quality_assurance"]
    
    quality_reports = state.get("quality_reports", {})
    if not quality_reports:
        return False, 0.0, "quality_reports object is empty or missing"
    
    # Check if all validations passed
    all_passed = True
    failed_checks = []
    
    for check_name, report in quality_reports.items():
        if isinstance(report, dict):
            if report.get("status") != "pass":
                all_passed = False
                failed_checks.append(check_name)
    
    if not all_passed and threshold["all_must_pass"]:
        return False, 0.0, f"QA validation failed for: {failed_checks}"
    
    passed_count = sum(1 for r in quality_reports.values() 
                       if isinstance(r, dict) and r.get("status") == "pass")
    total_count = len(quality_reports)
    confidence = passed_count / total_count if total_count > 0 else 0
    
    return True, confidence, f"QA validation passed ({passed_count}/{total_count} checks)"


VALIDATORS = {
    "initialization": validate_initialization,
    "brand_extraction": validate_brand_extraction,
    "market_research": validate_market_research,
    "campaign_strategy": validate_campaign_strategy,
    "research_writing": validate_research_writing,
    "campaign_planning": validate_campaign_planning,
    "article_execution": validate_article_execution,
    "quality_assurance": validate_quality_assurance
}


def run_validation(state_path: str, phase_name: str) -> Dict[str, Any]:
    """
    Run validation for a specific phase.
    
    Args:
        state_path: Path to workflow_state.json
        phase_name: Name of the phase to validate
        
    Returns:
        Validation result dictionary
    """
    # Normalize phase name
    phase_key = phase_name.lower().replace("-", "_").replace(" ", "_")
    
    # Load state
    try:
        state = load_workflow_state(state_path)
    except FileNotFoundError as e:
        return {
            "checkpoint": phase_name,
            "status": "fail",
            "confidence_score": 0.0,
            "message": str(e),
            "action": "request_input",
            "timestamp": datetime.now().isoformat()
        }
    
    # Get validator
    validator = VALIDATORS.get(phase_key)
    if not validator:
        return {
            "checkpoint": phase_name,
            "status": "fail",
            "confidence_score": 0.0,
            "message": f"Unknown phase: {phase_name}",
            "action": "request_input",
            "timestamp": datetime.now().isoformat()
        }
    
    # Run validation
    passed, confidence, message = validator(state)
    
    # Determine action
    if passed:
        action = "continue"
        status = "pass"
    elif confidence >= 0.5:
        action = "warning_continue"
        status = "warning"
    else:
        action = "rollback"
        status = "fail"
    
    return {
        "checkpoint": phase_name,
        "status": status,
        "confidence_score": round(confidence, 2),
        "message": message,
        "action": action,
        "timestamp": datetime.now().isoformat()
    }


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print(__doc__)
        print("\nError: Missing required arguments")
        print("Usage: python phase_validator.py <workflow_state.json> <phase_name>")
        sys.exit(1)
    
    state_path = sys.argv[1]
    phase_name = sys.argv[2]
    
    result = run_validation(state_path, phase_name)
    
    # Output result as JSON
    print(json.dumps(result, indent=2))
    
    # Exit with appropriate code
    if result["status"] == "pass":
        sys.exit(0)
    elif result["status"] == "warning":
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()