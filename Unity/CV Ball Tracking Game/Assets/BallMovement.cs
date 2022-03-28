using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallMovement : MonoBehaviour
{

    // Creating an object of the UDPRecieve class
    public UDPReceive UdpReceive;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

        // Storing the Contour Data from the UDP Object created above
        string ContourData = UdpReceive.data;

        //  The Contour Data is received in the form of a tuple with data seperated by commas. Ex: (45, 56, 767)
        // So we need to remove the 2 brackets and split the data according to the commas

        ContourData = ContourData.Remove(0, 1); // removes the first bracket
        ContourData = ContourData.Remove(ContourData.Length - 1, 1); // removes the last bracket

        // Here, we split the Data Values
        string[] ContourInfo = ContourData.Split(',');

        // Now, we need to pass these ContourInfo Data to our Ball Object
        // We divide these values by 100 & 1000 respectively as Unity Coordinates move in small fractions
        float BallXPos = 5 - float.Parse(ContourInfo[0]) / 100;
        float BallYPos = float.Parse(ContourInfo[1]) / 150;
        float BallArea = -10 + float.Parse(ContourInfo[2]) / 1000;


        // Passing the calculated values above to our Ball Object
        gameObject.transform.localPosition = new Vector3(BallXPos, BallYPos, BallArea);

    }
}
