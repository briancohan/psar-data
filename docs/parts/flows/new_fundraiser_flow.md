{! parts/nodes/events/new_fundraising_event.md !}

{! parts/nodes/forms/new_fundraiser_form.md !}
{! parts/nodes/forms/update_rsvp_form.md !}

{! parts/nodes/members/officer.md !}

{! parts/nodes/sheets/event_log_sheet.md !}


%% Fundraising
new_fundraising_event --- officer
officer ---|enters| new_fundraiser_form
new_fundraiser_form ---|appends| event_log_sheet
new_fundraiser_form -.-|updates| update_rsvp_form
