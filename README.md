Thanks again for meeting yesterday. I think having weekly meetings is a good idea.
Here is an outline for the next steps in this project. It is easy to get overwhelmed with the scope of this project, so my suggestion is to proceed somewhat linearly---I have marked the tasks that can be done in parallel.

1. First, we need a clean dataset to work with. The USPTO has pdfs for all patents 1790-2019. It also has metadata for patents post-1976. So, we only need to OCR the 1790-1976 patents (approx. 3million documents). As we discussed yesterday, we should keep the full text of the patents and identify the following information:
  * Patent Issue number
  * Patent issue date
  * Application date
  * Inventor name and location
  * Assignee name
  
2. The second part of the project involves disambiguating assignee names. The USPTO has done some of that post 1976, but it is not 100% perfect. Also, whatever we do it has to be something that can be updated.

3. After normalizing the assignee names, the next is going to be more challenging: we need to keep track of company name changes, mergers, spinoffs, subsidiaries, etc. In particular:
  * Name changes: companies sometimes change their name, or appear in the data under different names; example: Minnesota Mining and Manufacturing Company, MMM, and 3M are all the same company. Given that our project will span centuries, we need a way to keep track of these. For the companies that appear in CRSP/Compustat, they have already done our job for us: the permco variable in CRSP/Compustat keeps track of a unique company id, so we should use this for public companies.
Kat if you want to look into this and how we can find data that goes back in time, it would helpful
  * Subsidiaries: sometimes a company’s patents will be assigned to its subsidiary. For now this is fine. Eventually, what we would want, is another field keeping track of the parent company (parent_assignee) so that we can decide how we treat these later.
There is a form 4080 that keeps track of companies and their subsidiaries in the later period. Kat if you want to look into this and how we can find data that goes back in time, it would helpful
  * Mergers. Sometimes companies A and B merge to create a new company C. Again, the permco variable in CRSP/Compustat will be a bit helpful here to understand what they are doing (we should do the same); that is, companies A, B, and C should have unique IDs
  * Acquisitions: Company A buys company B, retains the name. Company A keeps its ID, company B is its subsidiary.
  * Spinoffs. Company A spins off its subsidiary company B: A and B have unique assignee IDs, but company B no longer has the same parent ID as A.
  
4. One thing that will help here is the list of company names that appear in Moody’s manuals over time. It would be helpful to match patents to those as it gives us a set of `master ids’. I will work on obtaining more comprehensive coverage towards the end of the sample.

5. Inventor names: eventually we want to disambiguate them as well, but please ignore them for now.
This is it for now. As I said above, having experience with these projects it is easy to get overwhelmed and get lost in the details. We should keep our attention to things that matter the most.
