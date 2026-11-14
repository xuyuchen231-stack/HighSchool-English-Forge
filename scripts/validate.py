from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'knowledge/curriculum.json').read_text(encoding='utf-8'))
topics=data['topics']; ids=[t['id'] for t in topics]
assert len(ids)==len(set(ids)) and topics
assert all(t['title'] and t['section'] and t['status'] in {'index_only','draft','reviewed'} for t in topics)
for t in topics:
    assert all(x in ids for x in t['prerequisites'])
for f in ['SKILL.md','README.md','references/answerless-exam-protocol.md','references/full-length-teacher-book.md','references/layout-and-export.md','references/knowledge-entry-standard.md','references/writing-rubric.md']:
    assert (root/f).is_file(),f
print(f'PASS: {len(topics)} topic nodes, unique IDs, valid references and required files. Linguistic correctness NOT validated.')