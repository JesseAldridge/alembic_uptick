#!/usr/bin/python

import shutil, re, os


with open('alembic_uptick_diff.txt') as f:
  s = f.read()
old_path = re.search('^\+(alembic.+)$', s, re.MULTILINE).group(1)
old_val_str = re.search('alembic/versions/([0-9a-z]+)_', old_path).group(1)
last_path = s.strip().splitlines()[-1]

last_val_str = last_path.rsplit('/', 1)[1].split('_')[0]
last_val = int(last_val_str, 16)
new_val_str = '0' + hex(last_val + 1)[2:]
new_path = re.sub(
  'alembic/versions/([0-9a-z]+)_', 'alembic/versions/{}_'.format(new_val_str), old_path)

print 'moving:'
print old_path
print new_path

if os.path.exists(old_path):
  shutil.move(old_path, new_path)

with open(new_path) as f:
  old_text = f.read()

new_text = re.sub(old_val_str, new_val_str, old_text)
new_text = re.sub(
  '^Revises: [0-9a-f]+$', 'Revises: {}'.format(last_val_str), new_text, flags=re.MULTILINE)
new_text = re.sub(
  "^down_revision = '[0-9a-f]+'$", 'down_revision: '{}''.format(last_val_str), new_text,
  flags=re.MULTILINE)

with open(new_path, 'w') as f:
  f.write(new_text)
