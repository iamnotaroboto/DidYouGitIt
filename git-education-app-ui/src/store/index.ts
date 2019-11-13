import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const mutationType = {
  SET_PROGRESS: 'SET_PROGRESS',
};

export const actionType = {
  UPDATE_PROGRESS: 'UPDATE_PROGRESS',
};

export interface QuestionStatus {
  status: string; // correct, incorrect, unfinished
  userInput: string;
  expectedInput: string;
  textFeedback: string;
}

export default new Vuex.Store({
  state: {
    progress: new Map() as Map<string, QuestionStatus>, // map questionId -> status
  },
  mutations: {
    [mutationType.SET_PROGRESS](state, payload: {questionId: string, status: QuestionStatus}) {
      const newMap = new Map(state.progress);
      newMap.set(payload.questionId, payload.status);
      state.progress = newMap;
    },
  },
  actions: {
    [actionType.UPDATE_PROGRESS]({ commit }, payload: QuestionStatus) {
      commit(mutationType.SET_PROGRESS, payload);
    },
  },
});
