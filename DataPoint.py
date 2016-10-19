class DataPoint():
    def __init__(self, p, LARGER_DISTANCE, TALK, NUM_CLUSTERS, SAMPLING_METHOD, centroids, data, DATA_SET, DATA_LEN):
        self.value = p[:]
        self.LARGER_DISTANCE = LARGER_DISTANCE
        self.TALK = TALK
        self.NUM_CLUSTERS = NUM_CLUSTERS
        self.SAMPLING_METHOD = SAMPLING_METHOD
        self.centroids = centroids 
        self.data = data
        self.DATA_SET = DATA_SET 
        self.DATA_LEN =  DATA_LEN
        
    def set_value(self, p):
        self.value = p
    
    def get_value(self):
        return self.value
    
    def set_cluster(self, cluster):
        self.cluster = cluster
    
    def get_cluster(self):
        return self.cluster


    def initialize_dataset():
        for i in range(DATA_LEN):
            point = DataPoint(DATA_SET[i])
            point.set_cluster(None)
            data.append(point)
        return

    def initialize_centroids():
        if (TALK) : 
            print("Centroides inicializados en:")
        for c in range(NUM_CLUSTERS):
            if (SAMPLING_METHOD == 0) :
                which = random.randint(0,DATA_LEN-1)
            elif (SAMPLING_METHOD == 1):
                which = c
            else :
                which = DATA_LEN-1 - c

            centroids.append(list(DATA_SET[which]))
            if (TALK) : 
                print(centroids[c])        
        if (TALK) : 
            print()

        return

    def update_clusters():
        changed = False

        for i in range(DATA_LEN):
            minDistance = LARGER_DISTANCE
            currentCluster = 0

            for j in range(NUM_CLUSTERS):
                dist = distance.euclidean(data[i].get_value(), centroids[j])
                if(dist < minDistance):
                    minDistance = dist
                    currentCluster = j

            if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
                data[i].set_cluster(currentCluster)
                changed = True

        members = [0] * NUM_CLUSTERS
        for i in range(DATA_LEN):
            members[data[i].get_cluster()] += 1

        if (TALK) : 
            for j in range(NUM_CLUSTERS):
                print("El cluster ", j, " incluye ", members[j], "miembros.")
            print()

        return changed

    def update_centroids():    
        if (TALK) : 
            print("Los nuevos centroids son:")
        for j in range(NUM_CLUSTERS):
            means = [0] * DATA_SET.shape[1]

            clusterSize = 0
            for k in range(len(data)):
                if(data[k].get_cluster() == j):
                    p = data[k].get_value()
                    for i in range(DATA_SET.shape[1]):
                        means[i] += p[i]
                    clusterSize += 1

            if(clusterSize > 0):
                for i in range(DATA_SET.shape[1]):
                    centroids[j][i] = means[i] / clusterSize

            if (TALK) : 
                print(centroids[j])        
        if (TALK) : 
            print()

        return