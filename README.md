
<h1>Audio Feature Extraction and Music Recommendation System</h1>

---
<h2>Overview</h2>
This project involves the extraction of Mel-Frequency Cepstral Coefficients (MFCC) features from a collection of audio files, combined with metadata from a tracks dataset, and the storage of these features in a MongoDB database. Additionally, a music recommendation system utilizing these features is implemented using Apache Spark.

<h2>Methodology</h2>

<h3>Audio Feature Extraction</h3>

The script first loads metadata from a tracks.csv file into a pandas DataFrame.
It iterates through audio files in a specified directory (fma_medium), extracting features such as MFCC, spectral centroid, zero-crossing rate, and duration using the librosa library.
Features are extracted and stored in a MongoDB collection (music.features), along with track IDs and file paths.

<h3>Data Preprocessing</h4>

- Audio features such as MFCC are padded to ensure uniform length across different tracks.
- Extracted features are stored in a structured DataFrame in MongoDB, facilitating easy retrieval and analysis.
<h3>Implementation of Music Recommendation System</h4>

- The project utilizes Apache Spark to build and implement a music recommendation system.
- Feature vectors extracted from the audio files are converted into Spark DataFrames.
- Dimensionality reduction techniques like PCA (Principal Component Analysis) are applied to reduce feature dimensionality while preserving essential information.
- Approximate Nearest Neighbors (ANN) search using BucketedRandomProjectionLSH is employed to find similar tracks based on their feature vectors.
  
<h2>Results and Evaluation</h2>
Effectiveness of MFCC Features: MFCC features provide a compact representation of audio that captures essential aspects for music recommendation.
Dimensionality Reduction: PCA effectively reduces the dimensionality of feature vectors, facilitating faster processing and model training.
Music Recommendation Performance: The recommendation system efficiently identifies similar tracks based on extracted audio features.
<h2>Conclusion</h2>
This project demonstrates a comprehensive pipeline for audio feature extraction, storage in a NoSQL database (MongoDB), and implementation of a music recommendation system using Apache Spark. The use of MFCC and dimensionality reduction techniques enhances the effectiveness and efficiency of the system, providing a basis for further optimization and enhancement.

<h2>Authors</h2>

- Abubakar shahid 22i-1883
- Faizan Ali 22i-2011
- Muhammad 22i-4372
