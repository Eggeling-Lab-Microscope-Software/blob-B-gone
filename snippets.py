# from glob import glob

# tracks = glob(
#              './Example Data/2D_Mix/P_No*.npy')
# import os

# import ntpath
# def __path_leaf(path):
#     head, tail = ntpath.split(path)
#     return tail or ntpath.basename(head)

# # Renaming the file
# for i,file in enumerate(tracks):
#     id = int(__path_leaf(file).split('-',1)[1][:-4])
#     os.rename(file, os.path.join('./Example Data/overwrite', f"P_No-{id-1}.npy"))