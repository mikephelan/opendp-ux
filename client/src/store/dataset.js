import dataset from "@/api/dataset";

import {
  SET_DATASET_LIST,
  SET_CURRENT_DATASET
} from './types';

const initialState = {
    datasetList: null,
    currentDataset: null
};
const getters = {
    getDatasetList: state => {
        return state.datasetList
    },
    getCurrentDataset: state => {
        return state.currentDataset
    },
};
const actions = {
    setDatasetList({commit, state}) {
        return dataset.getUserDatasets()
            .then((resp) => {
                console.log(resp.data.results)
                commit('SET_DATASET_LIST', resp.data.results)
            })
    },
    setCurrentDataset({commit, state}, objectId) {
        return dataset.getDataset(objectId)
            .then((resp) => {
                console.log(resp.data.results)
                commit('SET_CURRENT_DATASET', resp.data.results)
            })
    }
};


const mutations = {
    [SET_DATASET_LIST](state, datasetList) {
        state.datasetList = datasetList
    },
    [SET_CURRENT_DATASET](state, dataset) {
        state.currentDataset = dataset
    },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};
