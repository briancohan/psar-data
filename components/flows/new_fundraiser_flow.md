{! events/new_fundraiser_event.md !}

{! forms/new_fundraiser_form.md !}
{! forms/update_rsvp_form.md !}

{! members/officer.md !}

{! sheets/event_log_sheet.md !}


%% Fundraising
new_fundraiser_event --- officer
officer ---|enters| new_fundraiser_form
new_fundraiser_form ---|appends| event_log_sheet
new_fundraiser_form -.-|updates| update_rsvp_form
