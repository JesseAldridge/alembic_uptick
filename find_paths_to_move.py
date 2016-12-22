import textwrap


def find_paths_to_move(text):
  added, removed = set(), set()
  lines = text.splitlines()
  for line in lines:
    prefix = line.split('_')[0][1:]
    if line.startswith('+'):
      added.add(prefix)
    elif line.startswith('-'):
      removed.add(prefix)

  for prefix in added & removed:
    for line in lines:
      if line.startswith('+{}'.format(prefix)):
        yield line[1:]


if __name__ == '__main__':
  for text, expected in [(
    '''
    --- alembic_uptick_dev.txt  2016-12-21 19:48:24.000000000 -0800
    +++ alembic_uptick_current.txt  2016-12-21 19:48:22.000000000 -0800
    @@ -1,10 +1,10 @@
    +alembic/versions/0123456789c1_allow_recurring_projects.py
    +alembic/versions/0123456789c2_initialize_data_types_type_to_global.py
    +alembic/versions/0123456789c3_change_admin_edit_permissions.py
    +alembic/versions/0123456789c4_add_system_approved_type.py
    +alembic/versions/0123456789c5_create_offline_criteria_table.py
    +alembic/versions/0123456789c6_adding_type_column_to_group.py
     alembic/versions/0123456789c7_remove_unused_tables.py
     alembic/versions/0123456789c8_adding_indices_for_locations_and_.py
     alembic/versions/0123456789c9_init_rating_score.py
     alembic/versions/0123456789ca_add_needs_approval.py
    -alembic/versions/0123456789cb_add_audit_event_table.py
    -alembic/versions/0123456789cc_remove_ticket_price_metadata_from_no_needs_core.py
    -alembic/versions/0123456789cd_add_subscription_index.py
    -alembic/versions/0123456789ce_near_ticket_distance.py
    -alembic/versions/0123456789cf_needs_public_workforce.py
    -alembic/versions/0123456789d0_add_account_balance_to_organizations.py
    ''', []),

    ('''
    --- alembic_uptick_dev.txt  2016-12-21 19:00:34.000000000 -0800
    +++ alembic_uptick_current.txt  2016-12-21 19:00:32.000000000 -0800
    @@ -7,4 +7,4 @@
     alembic/versions/0123456789cd_add_subscription_index.py
     alembic/versions/0123456789ce_near_ticket_distance.py
     alembic/versions/0123456789cf_needs_public_workforce.py
    -alembic/versions/0123456789d0_add_account_balance_to_organizations.py
    +alembic/versions/0123456789d0_add_reservation_minutes.py
    ''', ['alembic/versions/0123456789d0_add_reservation_minutes.py'])
  ]:
    assert expected == list(find_paths_to_move(textwrap.dedent(text)))
