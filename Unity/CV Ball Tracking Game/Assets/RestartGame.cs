using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class RestartGame : MonoBehaviour
{
    // This method will be used to reload the game when the user clicks on the reload button
    public void ReloadGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

    // This method will be used to go back to the Main Menu Scene when the back button is pressed
    public void BackToMenu()
    {
        SceneManager.LoadScene("Main Menu");
    }

}
