import redis
import sys

def main(Host):
    print("Connecting...")
    # connect to redis
    client = redis.Redis(host=Host, port=6379)
    client.set('test', 'demo')
    value = client.get('test')
    print(value)
    

if __name__ == "__main__":
    main(sys.argv[1])