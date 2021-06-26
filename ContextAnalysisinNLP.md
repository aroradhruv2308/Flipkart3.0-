## talking about --------> Chat Bot 

### Context Analysis in NLP: Why It’s Valuable and How It’s Done

Basically this project will include sentiment analysis and ans to lot many questions related to these sentiments using the context analysis here is the good example related to these kinda analysis 

```Imagine a pundit’s tweet that reads: “Governor Smith’s hard-line stance on transportation cost him votes in the election.” Entity-based sentiment analysis of this sentence will indicate that “Governor Smith” is associated with negative sentiment. But that’s all you have: the knowledge that the Governor is viewed negatively. Wouldn’t it be even more helpful to know why? This is where theme extraction and context determination comes into play. Performing theme extraction on this sentence might give us two results: “hard-line stance” , “budget cuts” . Suddenly, the picture is much clearer: Governor Smith is being mentioned negatively in the context of a hard-line stance and budget cuts.```

this example make us understand that how important is this analysis in speech recognition

The foundation of context determination is the noun. Of course, this is true of named entity extraction as well. But while entity extraction deals with proper nouns, context analysis is based around more general nouns. For example, where “Cessna” and “airplane” will be classified as entities, “transportation” will be considered a theme (more on themes later). Lexalytics supports four methods of context analysis, each with its merits and disadvantages:

## Ngram Analysis
the ngram analysis is basically the way the machine can understand the context.usually we use bi gram for the context learning
### what the heck is context
the context is basically the surrounding of the word which computer use as the way to determine the same words in two different manner still its not clear lets take an example related to it 
for eg lets say : "book my tikets","read this book" here the both type of book are only understandable to the computer if it reads it as a whole sentence
### Stop words to clean up the n grams 
stop words which are considered as the noise in the sentence so to remove it we use this process basically we not remove the only word present in the list but we try to remove them as phrases so that is the same word appeared again but its phrase is important then it would not get removed
### noun phrases extraaction 
according to observation we can observe that a sentence is almost valuable due to the nouns it consist. the main thing or the context of many sentences can be understandable if the we get there nouns and in this type of analysis the stopword list is also not that much complicated as in the ngram analysis
### Themes and Theme Extraction with Relevancy Scoring
the only noun extraction cannot be that much usefull in understand the context properly so now comes the themeextraction part 
 



