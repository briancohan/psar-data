{! events/certification_event.md !}
{! members/member.md !}
{! forms/certification_form.md !}
{! sheets/certification_sheet.md !}

certification_event --- member
member ---|enters| certification_form
certification_form ---|updates| certification_sheet
