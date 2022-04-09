using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class RestartGame : MonoBehaviour
{

    [SerializeField] RectTransform fader;

    private void Start()
    {
         // ALPHA/OPACITY ANIMATION
        fader.gameObject.SetActive(true);
        LeanTween.alpha(fader, 1, 0);
        LeanTween.alpha(fader, 0, 0.5f).setOnComplete(() =>{
            fader.gameObject.SetActive(false);
        });
    }


    // This method will be used to reload the game when the user clicks on the reload button
    public void ReloadGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

   
    // This method will be used to go back to the Main Menu Scene when the back button is pressed
    public void BackToMenu()
    {
        
         fader.gameObject.SetActive(true);
        LeanTween.alpha(fader, 0, 0);
        LeanTween.alpha(fader, 1, 0.5f).setOnComplete(() =>{
            SceneManager.LoadScene("Main Menu");
        });
       
    }

}
