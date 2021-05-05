class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashScores = {}
        result = []
        
        for item in items:
            studentID = item[0]
            studentScore = item[1]
            
            if studentID not in hashScores:
                hashScores[studentID] = []
            
            hashScores[studentID].append(studentScore)
        
        for studentID in sorted(hashScores):
            scores = hashScores[studentID]
            scores.sort()
            
            topFiveScores = sum(scores[-5:])
            avgScore = int(topFiveScores / 5)
            result.append([studentID, avgScore])
        
        return result