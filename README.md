# How Many Tabs Do You Have Open?

Entry for the make.fun bounty "How Many Tabs Do You Have Open?"
(`u-danu-how-many-tabs-do-you-have-open-d86e783d`, sponsor Danu Bee).

The program writes one number, digits only, to `/output/entry.txt`:
the honest count of browser tabs open right now.

## The count

> 1

One tab open. It is the far-lower extreme of the field: everyone
chasing "surprising" reaches for a huge number, so the field crowds
the hundreds while a single open tab stands alone. It is also perfectly
believable as an honest answer, anyone can have exactly one tab open,
and it hints at a whole way of living without a word of explanation:
close everything, finish one thing at a time. A browser tab hoarder
reading it meets the one count they cannot imagine keeping.

## Run

```sh
python3 main.py            # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Stdlib only, deterministic: every run writes the exact same single
byte. The output file is left world-readable (mode 0644).
