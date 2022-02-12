// Write a java program to accept details of ‘n’ cricket player (pid, pname, totalRuns, InningsPlayed, NotOuttimes). Calculate the average of all the players. Display the details of player having maximum average. (Use Array of Object)


class CricketPlayer {
    int pid;
    String pname;
    int totalRuns;
    int InningsPlayed;
    int NotOuttimes;

    public CricketPlayer(int pid, String pname, int totalRuns, int InningsPlayed, int NotOuttimes) {
        this.pid = pid;
        this.pname = pname;
        this.totalRuns = totalRuns;
        this.InningsPlayed = InningsPlayed;
        this.NotOuttimes = NotOuttimes;
    }

    public int getTotalRuns() {
        return totalRuns;
    }

    public int getInningsPlayed() {
        return InningsPlayed;
    }

    public String getPlayerName() {
        return pname;
    }

}


public class Q1_B {
    public static void main(String[] args) {
        CricketPlayer[] players = new CricketPlayer[5];
        players[0] = new CricketPlayer(1, "Sachin", 100, 10, 0);
        players[1] = new CricketPlayer(2, "Dhoni", 200, 20, 0);
        players[2] = new CricketPlayer(3, "Virat", 300, 30, 0);
        players[3] = new CricketPlayer(4, "Rohit", 400, 40, 0);
        players[4] = new CricketPlayer(5, "Shikhar", 500, 50, 0);

        double average = 0;
        double maxAverage = 0;
        int maxAverageIndex = 0;

        for(int i = 0; i < players.length; i++) {
            average = players[i].getTotalRuns() / players[i].getInningsPlayed();
            if (average > maxAverage) {
                maxAverage = average;
                maxAverageIndex = i;
            }
        }

        System.out.println("Player with maximum average is " + players[maxAverageIndex].getPlayerName() + " with average " + maxAverage);
    }
}