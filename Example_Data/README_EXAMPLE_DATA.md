## Welcome to the Example Data


### Simulation Directory
Please, find the data used in the work for demonstration in the `2D_MIX_dynamicSTD` (2D) and `3D_MIX_dynamicSTD` (3D) directories.

We include 4 figures so you can get an overview of the data without the need to plot them first:
* 2D___250_free_particles (Plot of the dataset containing 250 simulated in 2D)
* 2D___250_free_particles_250_blobs (Plot of combined dataset containing 250 blobs and 250 free tracks simulated in 2D)
* 3D___250_free_particles (Plot of the dataset containing 250 simulated in 3D)
* 3D___250_free_particles_250_blobs (Plot of combined dataset containing 250 blobs and 250 free tracks simulated in 3D)

### MINFLUX Data Directory
Please, find the data used in the work for analyzing MINLFUX blob forming in the `Blob_GQ23nm_2D_Tracks` (2D) and `Blob_GQ23nm_3D_Tracks` (3D) directories and both used MINFLIX tracking sequences in `MINFLUX Tracking Sequences`.

In `Blob_GQ23nm_2D_Tracks` (2D) and `Blob_GQ23nm_3D_Tracks` (3D), we include `*_COVARIANCE_MATRICES.txt` files containint the values used for 2D/3D blob simulations.
Each `.npy` includes one blob as a numpy array of shape `[N,4] - Z,Y,X,T`.