set -e

echo 'upticking: ' $1
git checkout $1
ls alembic/versions/*.py | grep 0123456789 | tail -n 10 > alembic_uptick_current.txt
git checkout upstream/dev
git pull upstream dev
ls alembic/versions/*.py | grep 0123456789 | tail -n 10 > alembic_uptick_dev.txt
git checkout -
git pull upstream dev
diff -u alembic_uptick_dev.txt alembic_uptick_current.txt > alembic_uptick_diff.txt || true
rm alembic_uptick_dev.txt alembic_uptick_current.txt
python ~/Dropbox/alembic_uptick/uptick.py
