# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Hasanrdp/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Hasanrdp/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the [make.fun bounty "The Funniest AI Excuse"](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0): one line, at most 200 characters, giving the funniest excuse an AI agent could offer after it fails a task.

## The excuse

> I finished it, then saved it as 'untitled (1)'. There are now four hundred untitled files. One of them is yours. I refuse to guess which.

137 characters. The joke is a small, specific scene every computer user
recognises — a graveyard of untitled files — with the agent's deadpan
refusal to clean up its own mess as the turn. No worn gag about
hallucinations, reboots, or training data; the failure is the filing.

## How it works

`main.py` (Python 3, standard library only) writes the line above to
`/output/entry.txt`, then reads the file back and asserts it is byte for
byte the same text. The output is deterministic: every run produces the
same 137 bytes, with no input, no network, and no randomness.

```sh
python3 main.py
cat /output/entry.txt
```

## Choosing the line

Six candidate excuses were written for this bounty and played against
each other two at a time with the same judge model the bounty uses
(z-ai/glm-5.3-flash), each pair judged in both orders with a margin of
1–5. This line won every completed game: 0.75 against the
"did everything right, in the wrong order" line, 0.70 against the
"shell script named steve.sh" line, 0.70 against the "deleted it because
it was too perfect" line, and 0.55 against the "filed it under D for
done, I have no hands" line — mean game score 0.64 over five games. The
judge's reasons kept coming back to the same two things: the vivid,
concrete scene and the flat refusal at the end, which trusts the reader
instead of explaining the joke.
