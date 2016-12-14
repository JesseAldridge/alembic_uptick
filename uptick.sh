
#git checkout JesseAldridge/reservation_window

ls alembic/versions/*.py | grep 0123456789 | tail -n 10 > alembic_uptick_current.txt
git checkout upstream/dev
git pull upstream dev
ls alembic/versions/*.py | grep 0123456789 | tail -n 10 > alembic_uptick_dev.txt
git checkout -
diff -u alembic_uptick_dev.txt alembic_uptick_current.txt > alembic_uptick_diff.txt
uptick.py
# rm alembic_uptick_*.txt

# git commit -am "auto alembic uptick"
# git push JesseAldridge/reservation_window
# git push origin
