using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    // This method will be called wheneve the play button is pressed. Use the the "using UnityEngine.SceneMangement;"
    public void PlayGame()
    {
        SceneManager.LoadScene("CV Ball Tracking Game");
    }

    // This method will be called when the Quit button is pressed in the main menu
    public void QuitGame()
    {
        Application.Quit();
    }

}
