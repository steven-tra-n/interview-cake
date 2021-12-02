package HashMaps;

import java.util.HashMap;

public class WordCloud {
    public static HashMap<String, Integer> Generate(String input){
        HashMap<String, Integer> result = new HashMap<>();

        // 1. Split all words in string seperated by a space
        // 2. Store all words in hash map in lower case
        // 3. Increment accordingly
        // 4. What about punctuation?

        // 1
        String[] words = input.split(" ");

        for(int i = 0; i < words.length; i++){
            // 2
            String word = words[i].toLowerCase();

            for(int j = 0; j < word.length(); j++){
                // 4
                if(!Character.isLetter(word.charAt(j))){
                    result.put(Character.toString(word.charAt(j)), result.getOrDefault(Character.toString(word.charAt(j)), 0) + 1);

                    word = word.substring(0, word.length() - 1);
                };
            };

            // 3
            result.put(word, result.getOrDefault(word, 0) + 1);
        };

        return result;
    };
};


// System.out.println(WordCloud.Generate("After beating the eggs, Dana read the next step:"));
// System.out.println(WordCloud.Generate("Add milk and eggs, then add flour and sugar."));