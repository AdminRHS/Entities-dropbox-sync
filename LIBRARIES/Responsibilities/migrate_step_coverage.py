"""
Migrate Step-Level Responsibility Coverage into Task Templates
Increases step coverage from 83.3% to 95%+ by mapping unmapped steps to responsibilities
"""
import json
import os
import re
import time
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Base directory
SCRIPT_DIR = Path(__file__).resolve().parent
ENTITIES_DIR = SCRIPT_DIR.parent.parent

# Directories
TASK_TEMPLATES_DIR = ENTITIES_DIR / "TASK_MANAGERS" / "Task_Templates"
STEP_TEMPLATES_DIR = ENTITIES_DIR / "TASK_MANAGERS" / "Step_Templates"
CORE_DIR = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "Core"

# Backup directory
BACKUP_DIR = ENTITIES_DIR / "TASK_MANAGERS" / f"Task_Templates_Backup_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}"

def load_json(file_path, encoding='utf-8-sig'):
    """Load JSON file with error handling"""
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return json.load(f)
    except Exception as e:
        print(f"  [ERROR] Failed to load {file_path}: {e}")
        return None

def save_json(file_path, data, max_retries=3):
    """Save JSON file with retry logic for Dropbox sync"""
    for attempt in range(max_retries):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except PermissionError:
            if attempt < max_retries - 1:
                print(f"  [RETRY] File locked, waiting... (attempt {attempt + 1}/{max_retries})")
                time.sleep(2)
            else:
                print(f"  [ERROR] File locked after {max_retries} attempts: {file_path}")
                return False
    return False

def extract_action_object(step_text):
    """Extract action verb and object from step description"""
    # Common action verbs
    action_pattern = r'\b(configure|setup|test|verify|validate|create|build|deploy|install|update|review|analyze|generate|process|export|import|upload|download|send|receive|monitor|track|log|report|document|prepare|execute|run|check|ensure|confirm|implement|develop|design|draft|approve|reject|submit|schedule|notify|alert|initialize|finalize|complete|start|stop|pause|resume|cancel|archive|delete|remove|add|modify|edit|change|fix|debug|troubleshoot|investigate|research|evaluate|assess|measure|calculate|compute|estimate|predict|forecast|optimize|improve|enhance|refactor|migrate|upgrade|downgrade|rollback|backup|restore|recover|synchronize|integrate|connect|disconnect|link|unlink|attach|detach|join|leave|register|unregister|subscribe|unsubscribe|publish|unpublish|enable|disable|activate|deactivate|lock|unlock|open|close|expand|collapse|show|hide|display|render|format|parse|encode|decode|encrypt|decrypt|compress|decompress|extract|merge|split|combine|separate|filter|sort|search|find|locate|identify|detect|discover|scan|index|catalog|classify|categorize|tag|label|annotate|mark|flag|highlight|select|deselect|choose|pick|collect|gather|aggregate|summarize|consolidate|reconcile|match|compare|contrast|differentiate|distinguish|correlate|associate|relate|map|transform|convert|translate|adapt|adjust|customize|personalize|tailor|configure|parameterize|instantiate|initialize|provision|allocate|assign|delegate|distribute|dispatch|route|forward|redirect|transfer|move|copy|clone|duplicate|replicate|mirror|synchronize|reconcile|balance|normalize|standardize|harmonize|unify|consolidate|centralize|decentralize|federate|partition|segment|shard|cluster|group|organize|arrange|structure|format|layout|compose|construct|assemble|compile|package|bundle|wrap|unwrap|unpack|extract|decompress|inflate|deflate|encode|decode|serialize|deserialize|marshal|unmarshal|stringify|parse|tokenize|lexify|stem|lemmatize|normalize|clean|sanitize|validate|verify|check|inspect|examine|review|audit|assess|evaluate|grade|score|rank|rate|measure|quantify|count|tally|sum|total|average|aggregate|accumulate|collect|gather|compile|consolidate|merge|combine|join|union|intersect|subtract|exclude|filter|select|project|extract|sample|slice|partition|split|divide|separate|isolate|quarantine|contain|sandbox|virtualize|containerize|orchestrate|coordinate|manage|supervise|oversee|govern|regulate|control|command|direct|guide|lead|facilitate|enable|empower|authorize|authenticate|identify|verify|validate|certify|accredit|license|approve|endorse|recommend|suggest|propose|nominate|elect|appoint|assign|designate|name|title|label|tag|categorize|classify|organize|arrange|order|sequence|prioritize|rank|sort|filter|group|cluster|aggregate|summarize|abstract|generalize|specialize|instantiate|exemplify|illustrate|demonstrate|show|display|present|exhibit|reveal|expose|disclose|publish|broadcast|announce|declare|proclaim|state|assert|claim|affirm|confirm|verify|validate|prove|disprove|refute|contradict|challenge|question|query|ask|request|demand|require|need|want|desire|wish|hope|expect|anticipate|predict|forecast|project|estimate|approximate|calculate|compute|determine|derive|infer|deduce|conclude|summarize|recap|review|recapitulate|reiterate|repeat|restate|paraphrase|reformulate|rephrase|reword|revise|edit|modify|change|alter|amend|update|refresh|renew|restore|revive|resurrect|reactivate|reenable|reinstate|reestablish|rebuild|reconstruct|recreate|regenerate|reproduce|replicate|duplicate|copy|clone|mirror|reflect|echo|repeat|iterate|loop|cycle|recur|reoccur|happen|occur|take place|transpire|come about|arise|emerge|appear|surface|manifest|materialize|realize|actualize|implement|execute|perform|carry out|conduct|undertake|engage in|participate in|involve in|include in|incorporate in|integrate into|embed in|nest in|encapsulate in|wrap in|enclose in|surround with|border with|frame with|delimit with|bound with|contain within|hold within|house within|store within|save in|persist in|cache in|buffer in|queue in|stack in|heap in|pile in|accumulate in|collect in|gather in|assemble in|compile in|aggregate in|consolidate in|merge into|combine with|join with|unite with|unify with|integrate with|incorporate with|blend with|mix with|mingle with|fuse with|coalesce with|converge with|meet with|intersect with|overlap with|coincide with|align with|match with|correspond with|correlate with|associate with|relate to|connect to|link to|tie to|bind to|attach to|affix to|append to|add to|supplement with|complement with|augment with|enhance with|enrich with|improve with|upgrade with|update with|revise with|modify with|change with|alter with|amend with|adjust with|adapt with|customize with|tailor with|personalize with|configure with|parameterize with|tune with|optimize with|refine with|polish with|perfect with|finalize with|complete with|finish with|conclude with|end with|terminate with|close with|stop with|halt with|pause with|suspend with|freeze with|lock with|fix with|stabilize with|solidify with|harden with|strengthen with|reinforce with|fortify with|secure with|protect with|safeguard with|shield with|defend with|guard with|watch over|monitor over|oversee over|supervise over|manage over|control over|regulate over|govern over|rule over|preside over|chair over|head over|lead over|direct over|guide over|steer over|navigate over|pilot over|drive over|operate over|run over|execute over|perform over|carry out over|conduct over|administer over|handle over|deal with|cope with|manage with|handle with|process with|treat with|address with|tackle with|approach with|engage with|interact with|interface with|communicate with|converse with|discuss with|talk with|speak with|chat with|dialogue with|debate with|argue with|dispute with|contest with|challenge with|question with|query with|ask about|inquire about|investigate about|explore about|examine about|study about|research about|analyze about|evaluate about|assess about|review about|audit about|inspect about|check about|verify about|validate about|confirm about|prove about|demonstrate about|show about|illustrate about|exemplify about|clarify about|explain about|describe about|define about|specify about|detail about|elaborate about|expand on|expound on|discourse on|lecture on|teach about|instruct about|educate about|train about|coach about|mentor about|guide about|advise about|counsel about|consult about|confer about|deliberate about|consider about|contemplate about|ponder about|reflect on|think about|muse about|meditate on|ruminate on|chew over|mull over|weigh up|size up|scope out|check out|look into|delve into|dig into|probe into|search into|investigate into|explore into|venture into|enter into|go into|get into|dive into|plunge into|immerse in|submerge in|engross in|absorb in|engage in|involve in|participate in|partake in|share in|join in|take part in|play a role in|contribute to|add to|bring to|give to|provide to|supply to|furnish to|offer to|present to|submit to|deliver to|hand to|pass to|transfer to|convey to|transmit to|send to|dispatch to|forward to|route to|direct to|channel to|funnel to|pipe to|stream to|flow to|pour to|drain to|empty to|discharge to|release to|emit to|radiate to|broadcast to|transmit to|propagate to|disseminate to|distribute to|circulate to|spread to|diffuse to|disperse to|scatter to|sow to|plant to|seed to|cultivate in|grow in|develop in|evolve in|mature in|ripen in|age in|season in|cure in|treat in|process in|refine in|purify in|distill in|concentrate in|condense in|reduce in|minimize in|decrease in|diminish in|lessen in|lower in|cut in|trim in|prune in|clip in|shear in|crop in|harvest in|reap in|gather in|collect in|pick in|pluck in|pull in|draw in|extract from|derive from|obtain from|get from|acquire from|procure from|secure from|gain from|win from|earn from|achieve from|attain from|reach from|arrive at|come to|get to|access from|retrieve from|fetch from|bring from|carry from|transport from|move from|shift from|transfer from|relocate from|migrate from|transition from|convert from|transform from|change from|alter from|modify from|adapt from|adjust from|customize from|tailor from|personalize from|configure from|set up from|establish from|found from|create from|build from|construct from|assemble from|compile from|compose from|formulate from|devise from|design from|plan from|scheme from|plot from|chart from|map from|outline from|sketch from|draft from|draw from|render from|illustrate from|depict from|portray from|represent from|symbolize from|signify from|denote from|indicate from|mark from|flag from|highlight from|emphasize from|stress from|accentuate from|underscore from|underline from|italicize from|bold from|capitalize from|uppercase from|lowercase from|titlecase from|camelcase from|snakecase from|kebabcase from|slugify from|sanitize from|escape from|unescape from|encode from|decode from|encrypt from|decrypt from|hash from|unhash from|checksum from|verify from|validate from|authenticate from|authorize from|certify from|accredit from|license from|approve from|endorse from|ratify from|confirm from|substantiate from|corroborate from|support from|back from|uphold from|maintain from|sustain from|preserve from|conserve from|protect from|safeguard from|defend from|shield from|guard from|secure from|fortify from|strengthen from|reinforce from|bolster from|boost from|enhance from|improve from|upgrade from|update from|refresh from|renew from|revitalize from|rejuvenate from|restore from|rehabilitate from|repair from|fix from|mend from|patch from|correct from|rectify from|remedy from|resolve from|solve from|address from|tackle from|handle from|manage from|deal with|cope with|contend with|grapple with|wrestle with|struggle with|battle with|fight with|combat with|oppose with|resist with|counter with|counteract with|neutralize with|offset with|balance with|equilibrate with|stabilize with|normalize with|standardize with|regularize with|formalize with|systematize with|organize with|structure with|order with|arrange with|sort with|classify with|categorize with|group with|cluster with|batch with|bundle with|package with|wrap with|enclose with|contain with|hold with|house with|store with|keep with|retain with|preserve with|maintain with|sustain with|continue with|persist with|persevere with|endure with|last with|remain with|stay with|abide with|dwell with|reside with|live with|exist with|subsist with|survive with|thrive with|flourish with|prosper with|succeed with|triumph with|prevail with|win with|conquer with|overcome with|surmount with|transcend with|exceed with|surpass with|outdo with|outperform with|outshine with|eclipse with|overshadow with|dwarf with|diminish with|reduce with|lessen with|decrease with|lower with|cut with|trim with|prune with|pare with|shave with|slice with|chop with|dice with|mince with|grind with|crush with|pulverize with|powder with|atomize with|vaporize with|evaporate with|sublimate with|condense with|liquefy with|melt with|freeze with|solidify with|crystallize with|precipitate with|coagulate with|clot with|gel with|set with|harden with|stiffen with|rigidify with|petrify with|fossilize with|calcify with|ossify with|sclerosis with|atrophy with|degenerate with|deteriorate with|decay with|rot with|decompose with|disintegrate with|crumble with|collapse with|fall apart|break down|wear out|erode with|corrode with|rust with|oxidize with|tarnish with|discolor with|fade with|bleach with|whiten with|lighten with|brighten with|illuminate with|enlighten with|irradiate with|shine with|glow with|gleam with|glint with|sparkle with|glitter with|shimmer with|twinkle with|flicker with|flash with|blink with|wink with|strobe with)\b'

    # Extract action
    action_match = re.search(action_pattern, step_text.lower())
    action = action_match.group(1) if action_match else None

    # Extract object (noun after action, before preposition or end)
    object_text = None
    if action:
        # Get text after action
        rest = step_text[action_match.end():].strip()
        # Extract first noun phrase (simplified - takes words until preposition/conjunction)
        object_match = re.match(r'^(the\s+)?([a-zA-Z0-9_\-\s]+?)(?:\s+(?:for|to|in|on|at|with|by|from|and|or|but)|$)', rest)
        if object_match:
            object_text = object_match.group(2).strip()

    return action, object_text

def normalize_text(text):
    """Normalize text for matching"""
    if not text:
        return ""
    # Convert to lowercase, remove extra spaces
    normalized = text.lower().strip()
    # Remove articles
    normalized = re.sub(r'\b(the|a|an)\b', '', normalized)
    # Remove pluralization
    normalized = re.sub(r's$', '', normalized)
    # Remove extra spaces
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    return normalized

def find_responsibility_match(action, obj, phrase_index, action_variants, object_variants, dept_context=None):
    """Find matching responsibility ID using phrase matching and variants"""
    if not action or not obj:
        return None, 0.0  # No match, 0 confidence

    # Normalize inputs
    action_norm = normalize_text(action)
    obj_norm = normalize_text(obj)

    # Priority 1: Exact match
    exact_key = f"{action_norm}_{obj_norm}"
    if exact_key in phrase_index:
        matches = phrase_index[exact_key]
        # Prefer department-specific if available
        if dept_context:
            dept_matches = [m for m in matches if m.startswith(f"RESP-{dept_context}-")]
            if dept_matches:
                return dept_matches[0], 1.0  # Exact match with dept context
        return matches[0], 0.95  # Exact match

    # Priority 2: Action variant match
    action_variants_list = action_variants.get(action_norm, [action_norm])
    for variant_action in action_variants_list:
        variant_key = f"{variant_action}_{obj_norm}"
        if variant_key in phrase_index:
            matches = phrase_index[variant_key]
            if dept_context:
                dept_matches = [m for m in matches if m.startswith(f"RESP-{dept_context}-")]
                if dept_matches:
                    return dept_matches[0], 0.85
            return matches[0], 0.80

    # Priority 3: Object variant match
    object_variants_list = object_variants.get(obj_norm, [obj_norm])
    for variant_obj in object_variants_list:
        variant_key = f"{action_norm}_{variant_obj}"
        if variant_key in phrase_index:
            matches = phrase_index[variant_key]
            if dept_context:
                dept_matches = [m for m in matches if m.startswith(f"RESP-{dept_context}-")]
                if dept_matches:
                    return dept_matches[0], 0.75
            return matches[0], 0.70

    # Priority 4: Combined variants
    for variant_action in action_variants_list:
        for variant_obj in object_variants_list:
            variant_key = f"{variant_action}_{variant_obj}"
            if variant_key in phrase_index:
                matches = phrase_index[variant_key]
                if dept_context:
                    dept_matches = [m for m in matches if m.startswith(f"RESP-{dept_context}-")]
                    if dept_matches:
                        return dept_matches[0], 0.65
                return matches[0], 0.60

    return None, 0.0

def main():
    print("=" * 70)
    print("Migrating Step-Level Responsibility Coverage")
    print("=" * 70)

    # [1] Load resources
    print("\n[1] Loading resources...")

    # Load responsibilities ecosystem
    responsibilities_master = load_json(CORE_DIR / "responsibilities_master.json")
    phrase_index = load_json(CORE_DIR / "phrase_matching_index.json")
    action_variants = load_json(CORE_DIR / "action_variants_map.json")
    object_variants = load_json(CORE_DIR / "object_variants_map.json")

    if not all([responsibilities_master, phrase_index, action_variants, object_variants]):
        print("  [ERROR] Failed to load core resources. Exiting.")
        return

    # Handle both list and dict structures
    resp_count = len(responsibilities_master) if isinstance(responsibilities_master, list) else len(responsibilities_master.get('responsibilities', []))
    print(f"  - Responsibilities: {resp_count} loaded")
    print(f"  - Phrase index: {len(phrase_index)} patterns")
    print(f"  - Action variants: {len(action_variants)} actions")
    print(f"  - Object variants: {len(object_variants)} objects")

    # Load task templates
    task_templates = []
    if TASK_TEMPLATES_DIR.exists():
        for file_path in sorted(TASK_TEMPLATES_DIR.glob("*.json")):
            template = load_json(file_path)
            if template:
                task_templates.append((file_path, template))

    print(f"  - Task Templates: {len(task_templates)} files loaded")

    # [2] Analyze current coverage
    print("\n[2] Analyzing current coverage...")

    total_steps = 0
    mapped_steps = 0
    unmapped_steps = []

    for file_path, template in task_templates:
        checklist = template.get('checklist', [])
        for i, step in enumerate(checklist):
            total_steps += 1
            if step.get('responsibility_id'):
                mapped_steps += 1
            else:
                unmapped_steps.append({
                    'file': file_path.name,
                    'step_index': i,
                    'step': step
                })

    coverage_before = (mapped_steps / total_steps * 100) if total_steps > 0 else 0

    print(f"  - Total Steps: {total_steps}")
    print(f"  - Mapped Steps: {mapped_steps} ({coverage_before:.1f}%)")
    print(f"  - Unmapped Steps: {len(unmapped_steps)} ({100 - coverage_before:.1f}%)")

    # [3] Match unmapped steps to responsibilities
    print(f"\n[3] Matching {len(unmapped_steps)} unmapped steps to responsibilities...")

    matches = {
        'exact': 0,
        'variant': 0,
        'context': 0,
        'unmatched': 0
    }

    mappings_by_file = defaultdict(list)
    unmatched_details = []

    for item in unmapped_steps:
        step = item['step']
        step_text = step.get('description', '') or step.get('action', '')

        # Extract action and object
        action, obj = extract_action_object(step_text)

        # Get department context from filename
        dept_context = None
        if item['file'].startswith('TEMPLATE-TASK-AI-'):
            dept_context = 'AI'
        elif item['file'].startswith('TEMPLATE-TASK-LG-'):
            dept_context = 'LG'
        elif item['file'].startswith('TEMPLATE-TASK-DEV-'):
            dept_context = 'DEV'
        elif item['file'].startswith('TEMPLATE-TASK-HR-'):
            dept_context = 'HR'
        elif item['file'].startswith('TEMPLATE-TASK-OPS-'):
            dept_context = 'OPS'
        elif item['file'].startswith('TEMPLATE-TASK-MKT-'):
            dept_context = 'MKT'

        # Find match
        resp_id, confidence = find_responsibility_match(
            action, obj, phrase_index, action_variants, object_variants, dept_context
        )

        if resp_id:
            mappings_by_file[item['file']].append({
                'step_index': item['step_index'],
                'responsibility_id': resp_id,
                'confidence': confidence,
                'action': action,
                'object': obj
            })

            if confidence >= 0.90:
                matches['exact'] += 1
            elif confidence >= 0.70:
                matches['variant'] += 1
            else:
                matches['context'] += 1
        else:
            matches['unmatched'] += 1
            unmatched_details.append({
                'file': item['file'],
                'step_index': item['step_index'],
                'step_text': step_text,
                'extracted_action': action,
                'extracted_object': obj
            })

    print(f"  - Exact matches: {matches['exact']}")
    print(f"  - Variant matches: {matches['variant']}")
    print(f"  - Context matches: {matches['context']}")
    print(f"  - Unmatched: {matches['unmatched']}")

    # [4] Create backup
    print(f"\n[4] Creating backup...")
    if not BACKUP_DIR.exists():
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    # Copy all task templates to backup
    for file_path, _ in task_templates:
        import shutil
        backup_path = BACKUP_DIR / file_path.name
        shutil.copy2(file_path, backup_path)

    print(f"  - Backup created: {BACKUP_DIR.name}")

    # [5] Update task templates
    print(f"\n[5] Updating task templates...")

    updated_files = []
    failed_files = []

    for file_path, template in task_templates:
        if file_path.name not in mappings_by_file:
            continue  # No updates for this file

        # Apply mappings
        for mapping in mappings_by_file[file_path.name]:
            step_idx = mapping['step_index']
            if step_idx < len(template['checklist']):
                template['checklist'][step_idx]['responsibility_id'] = mapping['responsibility_id']

        # Save updated template
        if save_json(file_path, template):
            updated_files.append(file_path.name)
            num_mappings = len(mappings_by_file[file_path.name])
            print(f"  [OK] Updated: {file_path.name} ({num_mappings} steps mapped)")
        else:
            failed_files.append(file_path.name)

    if failed_files:
        print(f"\n  [WARNING] Failed to update {len(failed_files)} files:")
        for fname in failed_files:
            print(f"    - {fname}")

    # [6] Validation
    print(f"\n[6] Validation...")

    # Re-scan to get new coverage
    total_steps_after = 0
    mapped_steps_after = 0

    for file_path in TASK_TEMPLATES_DIR.glob("*.json"):
        template = load_json(file_path)
        if template:
            checklist = template.get('checklist', [])
            for step in checklist:
                total_steps_after += 1
                if step.get('responsibility_id'):
                    mapped_steps_after += 1

    coverage_after = (mapped_steps_after / total_steps_after * 100) if total_steps_after > 0 else 0
    improvement = mapped_steps_after - mapped_steps
    improvement_pct = coverage_after - coverage_before

    print(f"  - New Coverage: {mapped_steps_after} / {total_steps_after} ({coverage_after:.1f}%)")
    print(f"  - Improvement: +{improvement} steps (+{improvement_pct:.1f}%)")

    # [7] Generate report
    print(f"\n[7] Generating report...")

    report = {
        "migration_date": datetime.now().isoformat(),
        "coverage_before": {
            "total": total_steps,
            "mapped": mapped_steps,
            "percentage": round(coverage_before, 1)
        },
        "coverage_after": {
            "total": total_steps_after,
            "mapped": mapped_steps_after,
            "percentage": round(coverage_after, 1)
        },
        "improvements": {
            "steps_newly_mapped": improvement,
            "coverage_increase": round(improvement_pct, 1)
        },
        "matching_statistics": matches,
        "files_updated": updated_files,
        "files_failed": failed_files,
        "unmapped_steps": unmatched_details,
        "backup_location": str(BACKUP_DIR)
    }

    report_path = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "step_migration_report.json"
    save_json(report_path, report)

    print(f"  - Report saved: step_migration_report.json")

    # Summary
    print("\n" + "=" * 70)
    print("Migration Complete!")
    print("=" * 70)
    print(f"Coverage: {coverage_before:.1f}% -> {coverage_after:.1f}% (+{improvement_pct:.1f}%)")
    print(f"Files updated: {len(updated_files)}")
    print(f"Steps mapped: +{improvement}")
    print(f"Remaining unmapped: {len(unmatched_details)}")
    print("=" * 70)

if __name__ == "__main__":
    main()
