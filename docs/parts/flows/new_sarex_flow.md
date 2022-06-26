{! parts/nodes/events/new_sarex_event.md !}

{! parts/nodes/forms/enter_task_form.md !}
{! parts/nodes/forms/new_sarex_form.md !}
{! parts/nodes/forms/update_rsvp_form.md !}

{! parts/nodes/members/officer.md !}

{! parts/nodes/sheets/event_log_sheet.md !}

new_sarex_event --- officer
officer ---|enters| new_sarex_form
new_sarex_form ---|appends| event_log_sheet
new_sarex_form -.-|updates| update_rsvp_form
new_sarex_form -.-|updates| enter_task_form
