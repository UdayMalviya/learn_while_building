import http from 'k6/http';
import { check } from 'k6';

export let options = {
  scenarios: {
    constant_rate: {
      executor: 'constant-arrival-rate',
      rate: 1000,          // change to 5000, 10000 later
      timeUnit: '1s',
      duration: '30s',
      preAllocatedVUs: 200,
      maxVUs: 500,
    },
  },
};

const payload = open('./payload.json');

export default function () {
  const res = http.post(
    "http://127.0.0.1:8000/json",
    payload,
    { headers: { "Content-Type": "application/json" } }
  );

  check(res, {
    "status 200": (r) => r.status === 200,
  });
}