{! events/new_meeting_event.md !}

{! forms/new_meeting_form.md !}
{! forms/update_rsvp_form.md !}

{! members/officer.md !}

{! sheets/event_log_sheet.md !}

new_meeting_event --- officer
officer ---|enters| new_meeting_form
new_meeting_form ---|appends| event_log_sheet
new_meeting_form -.-|updates| update_rsvp_form
