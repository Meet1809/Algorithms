
<!DOCTYPE html>
<html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width,intial-scale=1.0">
     <title>Bubble Sort</title>
    <?php include "MasterTemplate/files.php" ?>
   </head>
   <body class="body-class">
       <?php include "navigation/navigation.php"?>
    <div class="main-div">
      <h1>Bubble Sort</h1>
      <div class="content">
        <script src="https://gist.github.com/Bhagydeep24/f98bae47965a4daebdf3dce24c7d7a1b.js"></script>
        </br></br>
        <article class="">
        Bubble sort is among the most commonly used sorting Algorithms. As per the name, it bubbles ups the highest element with
        each pass.
        </br></br>
        Let's suppose we use integer array as an input. Bubble sort uses 2 loops. First, loop is for the pass and second loop is used to
        compare 2 elements from starting index. For better understanding let's take an array of 5 element [5, 4, 3, 2, 1].
        </br></br>
        <h3>How it works:</h3>
        </br>
        <i>For first pass,</i>
        </br>
        <pre>
        5 & 4 are compared and since 5 is greater than 4 they swap their position,next
        5 & 3 are compared and since 5 is greater than 3 they swap their position,next
        5 & 2 are compared and since 5 is greater than 2 they swap their position,next
        5 & 1 are compared and since 5 is greater than 1 they swap their position.
      </pre>
        It can be seen our first loop is traversed and 5 which is the greatest element of our array is bubbled up to the last index.
        Hence this index won't be compared in next passes.
        </br></br>
        <i>For second pass,</i>
      </br>
      <pre>
        4 & 3 are compared and since 4 is greater than 3 they swap their position,next
        4 & 2 are compared and since 4 is greater than 2 they swap their position,next
        4 & 1 are compared and since 4 is greater than 1 they swap their position.
      </pre>
        <i>For third pass,</i>
      </br>
      <pre>
        3 & 2 are compared and since 3 is greater than 2 they swap their position,next
        3 & 1 are compared and since 3 is greater than 2 they swap their position.
          </pre>
        <i>For forth pass,</i>
      </br>
      <pre>
        2 & 1 are compared and since 2 is greater than 1 they swap their position.
      </pre>
        </br>
        <h3>Sorted Array:</h3>
        We have achieved our solution and finally the array achieved is [1, 2, 3, 4, 5].
        </br></br>
        <h3>Stable Sorting Algorithm:</h3>
        Bubble sort is a stable algorithm means we if there is a duplicate element then then these two duplicate elements are never going to swap their places.
        For example we have an array [4, 6, 2, 7, 4]. Here we have 4 as a duplicate element in our array and to show the difference
        we can mark 2nd 4 with * which makes our array look like [4, 6, 2, 7, 4*]. After applying bubble sorting the array we achieved is
        [2, 4, 4*, 6, 7]. And it can be seen our marked element never came before original 4.
        </br></br>
        <h3>In Place Sorting Algorithm:</h3>
        Bubble sort is a in place algorithm means we never used and extra array for storage and all our elements just swaped their position. Therefore space
        complexity if bubble sort is O(1).
        </br></br>
        <h3>Time complexity:</h3>
        Time complexity of bubble sort is O(n<sup>2</sup>).
        Worst case and average case both is O(n<sup>2</sup>) because in both case both loops are going to iterate so our time complexity
        is n times*n times. Whereas in best case time complexity is O(n) in a situation where our array is already sorted.
        </br></br>
        <h3>Pros:</h3>
        It can be used in a situation where our array do not require much sorting.
        </br></br>
        <h3>Cons:</h3>
        We cannot use bubble sort where array size is huge and it is totally unsorted because time complety increases with n<sup>2</sup>.
        </br></br>
        <h3>Code Editor:</h3>
        </br>
        Here is our code interpreter, code is already written in python we can execute the code by clicking on play button. After that we can input
        our own array string separated by comma.
      </br></br>
      Array string in case don't won't to waste time: 679,49,-1,455,3. After copy pasting array just press enter and output will display how the
      whole array is sorted with each step.
      </br></br>
      Execution time in seconds is also return with which we can observe execution time of the algorithm.
      <br
    </br></br>
        <iframe src="https://trinket.io/embed/python/3a98d6c315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
        </article>
      </div>
    </div>

   </body>
</html>
