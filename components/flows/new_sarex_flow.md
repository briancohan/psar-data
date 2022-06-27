{! events/new_sarex_event.md !}

{! forms/enter_task_form.md !}
{! forms/new_sarex_form.md !}
{! forms/update_rsvp_form.md !}

{! members/officer.md !}

{! sheets/event_log_sheet.md !}

new_sarex_event --- officer
officer ---|enters| new_sarex_form
new_sarex_form ---|appends| event_log_sheet
new_sarex_form -.-|updates| update_rsvp_form
new_sarex_form -.-|updates| enter_task_form
