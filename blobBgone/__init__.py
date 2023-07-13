import os
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from blobBgone.featureHandler import featureHandler

def BlobBGone(path:str = None, return_IDs:bool = False, regularization_method:str = 'standardize', verbose:bool = True):    
    # Grab the files
    files = featureHandler.grab_files(path = None)
    if verbose:
        print(f"Found {len(files)} files in the '{files[0].split(os.sep)[-2]}' directory.")
        
    # Setup the task list
    task_list = [featureHandler.from_npy(path = file, verbose = False) for file in files]
    
    if verbose:
        print("\nExtracting features...")
    # Extract features
    features = []
    for task in task_list:
        task.extract()
        features.append(task.to_array())

    # Regularize the features
    features = featureHandler.regularize_output(features, method = regularization_method)
    assert np.all(np.isfinite(features)), "NaN values still present in features."


    if verbose:
        print("\nClustering...")
    # Cluster the features
    clustering_FH  = KMeans(
        n_clusters = 2,
        init = 'k-means++',
        n_init = 'auto',
        max_iter = 300,
        verbose = 0,
        random_state = None,
        )
    fit_predict_FH = clustering_FH.fit_predict(features)
    
    cluster_1 = [task_list[i] for i in range(len(task_list)) if fit_predict_FH[i] == 0]
    cluster_2 = [task_list[i] for i in range(len(task_list)) if fit_predict_FH[i] == 1]
    comb = [cluster_1, cluster_2]
    
    ## Evaluate Blobbness ##
    # this is an experimental metric that attempts to decide what cluster is the blob cluster
    if verbose:
        print("\nZombie-score is being calculated...")
    c1_blobbness = np.mean([task.features.SPHE/task.features.MAX_DIST for task in cluster_1])
    c2_blobbness = np.mean([task.features.SPHE/task.features.MAX_DIST for task in cluster_2])
    if verbose:
        print("Cluster 1 Zombie-score: {:.2f}".format(c1_blobbness))
        print("Cluster 2 Zombie-score: {:.2f}".format(c2_blobbness))
        print("Zombie-score ratio: 1 : {:.2f}".format(max([c1_blobbness, c2_blobbness])/min([c1_blobbness, c2_blobbness])))
        print(
            "Silhouette Coefficient: %0.3f"
            % metrics.silhouette_score(features, fit_predict_FH, metric="euclidean")
        )
        
        print("\nCluster {} has been estimated to be the blob cluster.".format(np.argmax([c1_blobbness, c2_blobbness])+1))

    if not return_IDs:
        blobs = [task for task in comb[np.argmax([c1_blobbness, c2_blobbness])]]
        free =  [task for task in comb[np.argmin([c1_blobbness, c2_blobbness])]]
        return blobs, free

    blobs = [task.ID for task in comb[np.argmax([c1_blobbness, c2_blobbness])]]
    free =  [task.ID for task in comb[np.argmin([c1_blobbness, c2_blobbness])]]
    return blobs, free