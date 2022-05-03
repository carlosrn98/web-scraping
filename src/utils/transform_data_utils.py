class TransformData:
    @staticmethod
    def standardize_data(data):
        """
            This static method outputs a list of JSONs of the fragment 'resources'
            that comes from a JSON (data).
        """
        output_data = []
        for d in data:
            output_data.append(d["resources"][0])
        
        return output_data

    @staticmethod
    def standardize_ids(data):
        """
            This static method transforms a JSON column '_id' and changes it to 'id'.
        """
        for d in data:
            d["id"] = d["_id"]
            del d["_id"]
        return data