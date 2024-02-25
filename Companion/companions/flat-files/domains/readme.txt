This directory is for the facilitator to keep track of user-defined domains.
Any .krf files in this directory will be read by the facilitator when it starts
up.  This is an easy way to add new ad hoc domains without cluttering up
companion-internals.krf.

Two words of warning:
1) These flat files are NOT loaded into the KB.  They're just skimmed for
   domain information.
2) These flat files CAN be deleted automatically from the Companions UI using
   the "Delete Domain" option in the facilitator's context menu.

What this means is, don't save your master copy of any .krf files here.  Just
drop in a copy (either directly or through the "Register Domain" option in the
facilitator's context menu) when you want to work with a domain.

Note that if you define multiple domains in the same flatfile and delete one
of them, the other domains will be deleted as well.

For examples of how to define a new domain, see companion-internals.krf.