# qt_sermo_analytics
PlotlyDash Flask server for analyzing qt_sermo data.


# Data aggregation

**Sample table**

|  user | total runtime | recording runtimes | recording filenames | asr inference runtimes |                   asr results                   | user prompts | prompt runtimes |           prompt results           | robot runtimes |       robot tts       | robot gestures |
|:-----:|:-------------:|:------------------:|:-------------------:|:----------------------:|:-----------------------------------------------:|:------------:|:---------------:|:----------------------------------:|:--------------:|:---------------------:|:--------------:|
| uuid1 | xyz ms        | x ms               | timestamp1.wav       | y ms                   |  [00:00:00.000 --> 00:00:02.000]   Who are you? | Who are you? | z ms            | Hello!  *beep boop* My name is QT! | v ms           | Hello! My name is QT! | Greet        |
| |  | x ms               | timestamp2.wav       | y ms                   |  [00:00:00.000 --> 00:00:03.000]   What can you do? | What can you do? | z ms            | I can dance! *wiggle wiggle* | v ms           | I can dance | Dance        |
| uuid2 | xyz ms        | x ms               | timestamp1.wav       | y ms                   |  [00:00:00.000 --> 00:00:04.000]   What is for lunch? | Lunch? | z ms            | Yummy, I love lunch in my tummy! *burp* | v ms           | Yummy! I love lunch in my tummy! | Happy        |


## Discussion
### Dash
#### Tabs or Pages
- Findings online point out that tabs are more seemless but for large datasets it can get slow.
    - QTo data should not be expansive enough to make a difference.
- Tabs are not performative for print/pdf conversion
    - If a .pdf is needed, be in contact

# Bugs
## Major

## Minor
- There is a blue shadow over select button; find dbc bootstrap class
- Disable clear all or change button to only select all?
- Graphs are wrong style
