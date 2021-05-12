import session from './session';

export default {
    /**
     * Gets a list of datasets that belong to the currently logged in user
     * @returns {Promise<AxiosResponse<any>>}
     */
    getUserDatasets() {
        return session.get('/api/dataset-info/')
    },
    /**
     * Gets the dataset for this objectId
     * @returns {Promise<AxiosResponse<any>>}
     */
    getDataset(objectId) {
        return session.get('/api/dataset-info/' + objectId)
    }
}