for branch in `git for-each-ref --sort=committerdate refs/heads/ | tail -n 10 | cut -c 60-`; do
  uptick $branch
  rm alembic_uptick_*.txt
done


# git commit -am "auto alembic uptick"
# git push JesseAldridge/reservation_window
# git push origin
