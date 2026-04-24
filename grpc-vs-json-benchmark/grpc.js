import grpc from 'k6/net/grpc';

const client = new grpc.Client();
client.load(['.'], 'payload.proto');

const payload = JSON.parse(open('./payload.json'));

export let options = {
  scenarios: {
    constant_rate: {
      executor: 'constant-arrival-rate',
      rate: 1000,
      timeUnit: '1s',
      duration: '30s',
      preAllocatedVUs: 200,
      maxVUs: 500,
    },
  },
};

export default function () {
  // Connect once per VU (lazy init)
  if (!client.connected) {
    client.connect('127.0.0.1:50051', { plaintext: true });
  }

  client.invoke('Service/Process', payload);
}