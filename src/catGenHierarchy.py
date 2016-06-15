import input.jsonInput as json


class CatGenHierarchy:

    def __init__(self, label, genFile):
        self._label = ""
        self._entries = {}
        self._levels = 0
        self.readFromJSON(genFile)


    def readFromJSON(self, json_file):
        json_struct = json.readJSON(json_file)
        entries = json_struct.get('entries')
        root_levels = 0

        # Walking through JSON struct and copying each entry is probably
        # not necessary in python, but at least we make sure level is an int
        for idx in entries:
            json_entry = entries[idx]

            level = int( json_entry.get('level') )
            self._levels = level if level > self._levels else self._levels
            if level == 0:
                root_levels += 1

            entry = {
                'level': level,
                'name': json_entry.get('name'),
                'gen': json_entry.get('gen')
            }
            self._entries[idx] = entry

        if root_levels != 1:
            raise Exception('JSON invalid. Level 0 must occur exactly once.')


    def getEntries(self):
        return self._entries


    def nrLevels(self):
        return self._levels


    def getLevelEntry(self, key):
        return self._entries[key]['level']


    def getGeneralizationOf(self, key):
        return self._entries[key]['gen']


if __name__ == '__main__':
    cgh = CatGenHierarchy('sex', '../data/gen_hierarchies/SexGH.json')
    print cgh.getEntries()
    print cgh.getNrLevels()
    print cgh.getLevelEntry('Male')