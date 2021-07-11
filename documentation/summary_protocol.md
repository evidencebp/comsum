

  
   Summary labeling protocol




We label for two concept - Is_summary and Is_Generic
Specific cases


 1. Summary
      1. We consider only English messages (99% of the commits). The messgae must be in English to be considered a summary.
      2. A summary should reflect information in the message, **not** to add **new information**.
      3. In a summary, the subject should capture the **essence** of the message.
      4. Specific cases:
          1. If the subject appears in the rest of the message (as in extractive summarization), this is a summary.
          1. Change/detail,  the subject describes a change and the message describes its details, it is a summary.
          1. If the commit classification of the subject is different from the message, this is not a summary.
          1. Goal/mean relation (e.g. "prevent crash" & "check amount is not zero before computing average price"), is considered as a summary.
          1. Change/reason (e.g., "added caller information" & "..to ease debug") is considered to be a summary.
          1. Administrative message, if all the changed content is in the subject (e.g., the message contains only administrative information like ticket number and reviewer name) , is not a summary.
          1. Merge subject ("Merge branch '15.3'") and a message that describes the content is not a summary. That is since the content could fit branch '16.3' just as well.
          1. Content announcing subject ("Declaration of") and a message that describes the content is not a summary. That is since different contents could fit 'Declaration of' just as well.
          1. Subject content by reference (e.g., just referring to a ticket number) is not a summary. While the content exists, it is not self contained.
          1. If the message content is only  by reference (e.g., hash of the reverted commit), it is not self-contained and cannot be summarized. Hene, this is not a summary.
      
  
 1. Generic
  
      1. If the subject can be applied to many other commits it is generic.
      1. Specific cases:
          1. Subject: "WIP" (work in progress) is generic and not a summary.
          1. If the subject can be applied to many other commits, yet fully describe the change (e.g., 'Updated Spanish translation'), it is generic and summary.
          1. Merge subject ("Merge branch '15.3'") is generic.
          1. Content announcing  subject ("Declaration of") is generic.


