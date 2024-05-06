from collections import defaultdict, namedtuple
from sys import stdin, stdout

Event = namedtuple('Event', ['time', 'spy', 'type', 'data'])

def is_consistent(events):
    spies = defaultdict(lambda: {'car': None, 'debt': 0})
    for event in events:
        spy = spies[event.spy]
        if event.type == 'p':
            if spy['car'] is not None:
                return False
            spy['car'] = event.data
            spy['debt'] += catalog[event.data].pickup
        elif event.type == 'r':
            if spy['car'] is None or spy['car'] != event.data:
                return False
            spy['car'] = None
            spy['debt'] += catalog[event.data].price_per_km * event.data
        elif event.type == 'a':
            if spy['car'] is None or spy['car'] != event.data:
                return False
            spy['debt'] += round(catalog[event.data].price * event.data / 100)
        else:
            return False
    return all(spy['car'] is None for spy in spies.values())

def main():
    num_cases = int(stdin.readline())
    for case in range(num_cases):
        num_cars, num_events = map(int, stdin.readline().split())

        global catalog
        catalog = {}
        for _ in range(num_cars):
            name, price, pickup, price_per_km = stdin.readline().split()
            catalog[name] = namedtuple('Car', ['name', 'price', 'pickup', 'price_per_km'])(name, int(price), int(pickup), int(price_per_km))

        events = []
        for _ in range(num_events):
            time, spy, type_, data = stdin.readline().split()
            events.append(Event(int(time), spy, type_, data))

        events.sort()

        for spy in sorted(set(event.spy for event in events)):
            spy_events = [event for event in events if event.spy == spy]
            stdout.write('{} {}\n'.format(spy, 'INCONSISTENT' if not is_consistent(spy_events) else sum(spy['debt'] for spy in spies.values())))

if __name__ == "__main__":
    main()