import Vue from 'vue';
import VueRouter from 'vue-router';
import Question from '../views/Question.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirct: '/intro',
  },
  {
    path: '/intro',
    name: 'intro',
    component: Question,
  },
  {
    path: '/q1',
    name: 'question1',
    component: Question,
  },
  {
    path: '/q2',
    name: 'question2',
    component: Question,
  },
  {
    path: '/q3',
    name: 'question3',
    component: Question,
  },
  {
    path: '/q4',
    name: 'question4',
    component: Question,
  },
  {
    path: '/q5',
    name: 'question5',
    component: Question,
  },
  {
    path: '/c1',
    name: 'scenario1',
    component: Question,
  },
  {
    path: '/c2',
    name: 'scenario2',
    component: Question,
  },
  {
    path: '/c3',
    name: 'scenario3',
    component: Question,
  },
  {
    path: '/c4',
    name: 'scenario4',
    component: Question,
  },
  {
    path: '/c5',
    name: 'scenario5',
    component: Question,
  },
];

const router = new VueRouter({
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
});

export default router;
