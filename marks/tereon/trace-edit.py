# Tereon (watchman): the roof edge runs on to the right edge, in front of the sea.
# In the drawing it stopped mid-picture and the sea continued below its level, so ledge and sea
# merged into one dark area. Right of x = 735: the two cream lines of the moulding continue, and
# everything below them is the navy roof; the sea stays above the ledge.
right = (xx >= 735*S) & (d < inner - 2*S)
lines = ((yy >= 929*S) & (yy < 937*S)) | ((yy >= 944*S) & (yy < 950*S))
below = (yy >= 937*S) & ~lines
navy[right & lines] = False
navy[right & below] = True
accent[right & (yy >= 929*S)] = False
# Keep a navy band above the ledge, so the lowest waves do not run into its top line.
navy[right & (yy >= 919*S) & (yy < 929*S)] = True
