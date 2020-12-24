using System;
namespace ParticleSwarmOptimization
{
  class Program
  {
    static Random ran = null;
    static void Main(string[] args)
    {
      try
      {
        Console.WriteLine("\nBegin PSO demo\n");
        ran = new Random(0);

        int numberParticles = 40;
        int numberIterations = 1000;
        int iteration = 0;
        int Dim = 2; // dimensions
        double minX = -100.0;
        double maxX = 100.0;

        Particle[] swarm = new Particle[numberParticles];
        double[] bestGlobalPosition = new double[Dim];
        double bestGlobalFitness = double.MaxValue; 

        double minV = -1.0 * maxX;
        double maxV = maxX;

        // Initialize all Particle objects
        for (int i = 0; i < swarm.Length; ++i)
        { 
        double[] randomPosition = new double[Dim];
        for (int j = 0; j < randomPosition.Length; ++j) {
          double lo = minX;
          double hi = maxX;
          randomPosition[j] = (hi - lo) * ran.NextDouble() + lo; 
        }

        double fitness = ObjectiveFunction(randomPosition);
        double[] randomVelocity = new double[Dim];
        for (int j = 0; j < randomVelocity.Length; ++j) {
          double lo = -1.0 * Math.Abs(maxX - minX);
          double hi = Math.Abs(maxX - minX);
          randomVelocity[j] = (hi - lo) * ran.NextDouble() + lo;
        }
        swarm[i] = new Particle(randomPosition, fitness, randomVelocity,
          randomPosition, fitness);

        double w = 0.729; // inertia weight
        double c1 = 1.49445; // cognitive weight
        double c2 = 1.49445; // social weight
        double r1, r2; // randomizations

        // Main processing loop
        for (int i = 0; i < swarm.Length; ++i) 
        {
          Particle currP= swarm[i];
                    
          for (int j = 0; j < currP.velocity.Length; ++j) 
          {
            r1 = ran.NextDouble();
            r2 = ran.NextDouble();

            newVelocity[j] = (w * currP.velocity[j]) +
              (c1 * r1* (currP.bestPosition[j] - currP.position[j])) +
              (c2 * r2 * (bestGlobalPosition[j] - currP.position[j]));
        
          if (newVelocity[j] < minV)
            newVelocity[j] = minV;
          else if (newVelocity[j] > maxV)
            newVelocity[j] = maxV;
          } // each j
            newVelocity.CopyTo(currP.velocity, 0);

          for (int j = 0; j < currP.position.Length; ++j)
          {
            newPosition[j] = currP.position[j] + newVelocity[j];
            if (newPosition[j] < minX)
              newPosition[j] = minX;
            else if (newPosition[j] > maxX)
              newPosition[j] = maxX;
          }
          newPosition.CopyTo(currP.position, 0);
         
        

        // Display results

        Console.WriteLine("\nProcessing complete");
        Console.Write("Final best fitness = ");
        Console.WriteLine(bestGlobalFitness.ToString("F4"));
        Console.WriteLine("Best position/solution:");
        for (int i = 0; i < bestGlobalPosition.Length; ++i){
          Console.Write("x" + i + " = " );
          Console.WriteLine(bestGlobalPosition[i].ToString("F4") + " ");
        }
        Console.WriteLine("");
        Console.WriteLine("\nEnd PSO demo\n");
      }
      }
      catch (Exception ex)
      {
        Console.WriteLine("Fatal error: " + ex.Message);
      }
    } // Main()

    static double ObjectiveFunction(double[] x)
     {
      return 3.0 + (x[0] * x[0]) + (x[1] * x[1]);
    }

  } // class Program

 public class Particle
{
  public double[] position;
  public double fitness;
  public double[] velocity;

  public double[] bestPosition;
  public double bestFitness;

  public Particle(double[] position, double fitness,
   double[] velocity, double[] bestPosition, double bestFitness)
  {
    this.position = new double[position.Length];
    position.CopyTo(this.position, 0);
    this.fitness = fitness;
    this.velocity = new double[velocity.Length];
    velocity.CopyTo(this.velocity, 0);
    this.bestPosition = new double[bestPosition.Length];
    bestPosition.CopyTo(this.bestPosition, 0);
    this.bestFitness = bestFitness;
  }

  public override string ToString()
  {
    string s = "";
    s += "==========================\n";
    s += "Position: ";
    for (int i = 0; i < this.position.Length; ++i)
      s += this.position[i].ToString("F2") + " ";
    s += "\n";
    s += "Fitness = " + this.fitness.ToString("F4") + "\n";
    s += "Velocity: ";
    for (int i = 0; i < this.velocity.Length; ++i)
      s += this.velocity[i].ToString("F2") + " ";
    s += "\n";
    s += "Best Position: ";
    for (int i = 0; i < this.bestPosition.Length; ++i)
      s += this.bestPosition[i].ToString("F2") + " ";
    s += "\n";
    s += "Best Fitness = " + this.bestFitness.ToString("F4") + "\n";
    s += "==========================\n";
    return s;
  }
  }
} // class Particle