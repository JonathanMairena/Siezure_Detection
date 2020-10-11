# Siezure Detection

Adapting a pytorch action detection network to classify whether a mouse was having a siezure for the Goldman Neurology Laboratory at the Children's Hospital of Pennsylvania. This project allowed for days of video to be shortened into the seconds and for the exact time when a mouse is having a siezure to be found. Seeing when a siezure begins without having EEG data is incredibly difficult and tedious, the movements of a mouse's siezure could be very subtle making it very difficult to study spontaneous siezures in mice. Instead most labs study dravet syndrome or other inducible siezure syndroms. Epilepeptic attacks in humans are not solely produced by light, heat or external factors and this laboratory is studying the genetic effects of epilepsy thus having a method of studying spontaneous as well as induced seizures allows for preventative mmedicine to be tested and deeveloped and then expanded to humans with epilepsy. 

# First
Run DataCreation.py

Here you can create compatible folder names and break videos into short 10 second clips eacch having a label for seizure or not seizure. These short 10 second clips are then broken up into images and placed into a folder titled 0,1,2,...,n, the images have the name 0,1,2,3,...,n.jpeg.

# Second
Train the model using the labeled video data. This video data show 5 different siezures happening at different times of day and with different mice. The video data was taken with one mouse in a cage, the mouse has an eeg attached to his head. The EEG data was useed ot determine exactly when the seizure began and ended. 

# Third 
Test the model with test data and find which 10 second clip was marked a having a seizure, verify by looking at the video. Augment your data with the newly
aquired data and repeat. Using different models the best was found to be RCNN-ResNet.
