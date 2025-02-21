class Asset:
    def __init__(self,AssetID,AssetName,ImportYear,Value):
        self.AssetID=AssetID
        self.AssetName=AssetName
        self.ImportYear=ImportYear
        self.Value=Value
    def __str__(self):
        return f"{self.AssetID}\t{self.AssetName}"