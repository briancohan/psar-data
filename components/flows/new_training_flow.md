{! events/new_training_event.md !}

{! forms/new_training_form.md !}
{! forms/update_rsvp_form.md !}

{! members/officer.md !}

{! sheets/event_log_sheet.md !}


new_training_event --- officer
officer ---|enters| new_training_form
new_training_form ---|appends| event_log_sheet
new_training_form -.-|updates| update_rsvp_form
