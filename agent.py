# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:48:49 2019

@author: Emily Timko etimko16@mail.bw.edu
"""

import deck
import random

class Agent:
    #Game rules:
    #Two cards are dealt to dealer and agent
    #Only one of the dealer's cards is visible to the agent
    #The agent may hit or stand once
    #After the agent picks an action, the dealer draws until the sum of his cards is greater than 16
    #The agent receives 10 points for a win, 0 points for a draw, -10 points for a loss, and 30 points for 21
    #Ace is always worth 11
    
    def __init__(self):
        self.states = Agent.initializeStates() #States are represented in [Agent's state, dealer's visible card] pairs
        self.actions = ["hit", "stand"] #Possible actions
        self.q = dict() #Q-values will be defined for every (state, action) pair
        self.alpha = 0.5 #Learning rate, decreases
        self.gamma = 0.8 #Discount rate
        self.epsilon = 100 #Epsilon is used to calculate chance of picking opposite action (exploration), decreases
    
    def main():   
        agent = Agent()
        numRounds = 100000
        extraRounds = 10000
        
        gamesWon = 0
        gamesTied = 0
        gamesLost = 0
        totalReward = 0
        round = 1
        
        print("\nWelcome to Blackjack!")
        print("\nThe agent will run ", extraRounds, " rounds while picking actions randomly.")
        print("The agent will then conduct reinforcement learning for ", numRounds, " rounds.")
        print("Then the agent will run ", extraRounds, " rounds with its learned policy.")
        print("You will be able to compare win rates before and after learning.\n")
        
        print("\nThe agent is picking randomly...\n")
        
        for x in range(extraRounds):
            
            gameDeck = deck.Deck()
            agentHand = [gameDeck.drawCard(), gameDeck.drawCard()]
            dealerHand = [gameDeck.drawCard(), gameDeck.drawCard()] #First card is known, second unknown to agent
            
            state = Agent.getState(agentHand, dealerHand, agent.states) 
            #Pick a state from the list of all possible states based on the hands
            
            if (state[0] != "bust" and state[0] != 21):
                action = Agent.pickRandomAction(state, agent.actions, agent.epsilon, agent.q) #Action picked randomly
                newState = Agent.getResultState(state, agentHand, action, gameDeck)
            else: #No actions allowed
                action = "stand"
                newState = state
                
            reward = Agent.endRound(agentHand, dealerHand, gameDeck)
            
            totalReward += reward #Add reward to total points
            
            #print (reward)
            if (reward == -10):
                gamesLost += 1
            elif (reward == 0):
                gamesTied += 1
            elif (reward == 10 or reward == 30):
                gamesWon += 1
    
            round += 1
            
            if round == extraRounds: #Print results at the end of non-learning rounds
                print ("The randomly picking agent played ", extraRounds, " rounds.")
                print ("It won ", gamesWon, " rounds.")
                print ("It tied ", gamesTied, " rounds.")
                print ("It lost ", gamesLost, " rounds.")
                print ("Total reward: ", totalReward)
                print("\nWin rate: ", gamesWon / round * 100, "%.")
                
                gamesWon = 0
                gamesLost = 0
                gamesTied = 0
                totalReward = 0
                round = 0
                print("\nThe agent is learning...\n")
    
        for y in range(numRounds):
            
            if agent.epsilon > .1: #Decreasing chance of exploration until it reaches 0.1
                agent.epsilon -= .1
            if agent.alpha > .0005: #Decreasing learning rate until it reaches 0.0005
                agent.alpha -= .0005
            
            gameDeck = deck.Deck()
            agentHand = [gameDeck.drawCard(), gameDeck.drawCard()]
            dealerHand = [gameDeck.drawCard(), gameDeck.drawCard()] #First card is known, second unknown to agent
            
            state = Agent.getState(agentHand, dealerHand, agent.states) 
            #Pick a state from the list of all possible states based on the hands
            
            if (state[0] != "bust" and state[0] != 21):
                action = Agent.pickAction(state, agent.actions, agent.epsilon, agent.q)
                newState = Agent.getResultState(state, agentHand, action, gameDeck)
            else: #No actions allowed
                action = "stand"
                newState = state
                
            reward = Agent.endRound(agentHand, dealerHand, gameDeck)
            
            totalReward += reward #Add reward to total points
            
            Agent.observe(state, action, agent.actions, newState, reward, agent.alpha, agent.gamma, agent.epsilon, agent.q)
            #Update q-values
            
            #print (reward)
            if (reward == -10):
                gamesLost += 1
            elif (reward == 0):
                gamesTied += 1
            elif (reward == 10 or reward == 30):
                gamesWon += 1
    
            round += 1
            
            #Post-learning results can be printed if desired
            if round == numRounds: #Print results at the end of learning rounds
                '''print ("The learning agent played ", numRounds, " rounds.")
                print ("It won ", gamesWon, " rounds.")
                print ("It tied ", gamesTied, " rounds.")
                print ("It lost ", gamesLost, " rounds.")
                print ("Total reward: ", totalReward)
                print("\nWin rate: ", gamesWon / round * 100, "%.")'''
                gamesWon = 0
                gamesLost = 0
                gamesTied = 0        
                totalReward = 0
                round = 0
                print("\nThe agent is acting intelligently...\n")
                
        for z in range(extraRounds):
            
            gameDeck = deck.Deck()
            agentHand = [gameDeck.drawCard(), gameDeck.drawCard()]
            dealerHand = [gameDeck.drawCard(), gameDeck.drawCard()] #First card is known, second unknown to agent
            
            state = Agent.getState(agentHand, dealerHand, agent.states) 
            #Pick a state from the list of all possible states based on the hands
            
            if (state[0] != "bust" and state[0] != 21):
                action = Agent.pickAction(state, agent.actions, agent.epsilon, agent.q)
                newState = Agent.getResultState(state, agentHand, action, gameDeck)
            else: #No actions allowed
                action = "stand"
                newState = state
                
            reward = Agent.endRound(agentHand, dealerHand, gameDeck)
            
            totalReward += reward #Add reward to total points
                        
            #print (reward)
            if (reward == -10):
                gamesLost += 1
            elif (reward == 0):
                gamesTied += 1
            elif (reward == 10 or reward == 30):
                gamesWon += 1
    
            round += 1
            
            if round == extraRounds: #Print results at the end of post-learning rounds
                print ("The intelligent agent played ", extraRounds, " rounds.")
                print ("It won ", gamesWon, " rounds.")
                print ("It tied ", gamesTied, " rounds.")
                print ("It lost ", gamesLost, " rounds.")
                print ("Total reward: ", totalReward)
                print("\nWin rate: ", gamesWon / round * 100, "%.")

                
    def pickRandomAction(state, actions, epsilon, q):
        return actions[random.randint(0, 1)]
            
    def getResultState(state, agentHand, action, deck):
        #Returns new state from state and action (adds card drawn to hand, if applicable)
        if action == "hit":
            card = deck.drawCard()
            agentHand.append(card)
            result = (Agent.sumCards(agentHand, False), state[1])
        elif action == "stand":
            result = state
        return result
    
    def fillEmptyQ(state, actions, q): 
        #Initializes q-values as 0 if the state has not been reached before
        if (state, actions[0]) not in q:
            q[(state, actions[0])] = 0
        if (state, actions[1]) not in q:
            q[(state, actions[1])] = 0
        return q
            
    def getState(agentHand, dealerHand, states):           
        #Returns a state from the list of all possible states based on the hands
        for x in range(276):
            if states[x] == (Agent.sumCards(agentHand, False), Agent.getValue(dealerHand[0])):
                return states[x]
        
    def maxQ(state, actions, q): 
        #Returns the higher q-value of the action options
        q = Agent.fillEmptyQ(state, actions, q)
        if q[(state, actions[0])] > q[(state, actions[1])]:
            return q[(state, actions[0])]
        else:
            return q[(state, actions[1])]
        
    def pickAction(state, actions, epsilon, q):
        #Returns the best action (highest q-value) with a chance of picking the 
        #opposite action (exploration) based on epsilon
        q = Agent.fillEmptyQ(state, actions, q)
        if q[(state, actions[0])] > q[(state, actions[1])]:
            if (random.randint(0, 100) <= epsilon): #Occurs epsilon% of the time
                return actions[1]
            else:
                return actions[0]
        elif q[(state, actions[0])] < q[(state, actions[1])]:
            if (random.randint(0, 100) <= epsilon): #Occurs epsilon% of the time
                return actions[0]
            else:
                return actions[1]
        else:
            return actions[random.randint(0, 1)]
        
    def observe(state, action, actions, newState, reward, alpha, gamma, epsilon, q):
        #Updates q-value
        q = Agent.fillEmptyQ(state, actions, q)
        newQ = (1-alpha)*(q[(state, action)]) + alpha*(reward + gamma*(Agent.maxQ(newState, actions, q)))
        q[(state, action)] = newQ
       
    def initializeStates(): #Returns list of possible states (combinations of agent hand and dealer visible card)
        agentStates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "bust"]
        dealerStates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        worldStates = [None] * 276

        i=0
        for x in agentStates:
            for y in dealerStates:
                worldStates[i] = (x, y)
                i += 1
                    
        return worldStates
                
    def endRound(agentHand, dealerHand, deck): 
        #Ends round, returns reward
        
        while (Agent.sumCards(dealerHand, True) < 17): #Dealer plays
            dealerHand.append(deck.drawCard())
        
        dealerSum = Agent.sumCards(dealerHand, True)
        agentSum = Agent.sumCards(agentHand, False)
        
        if agentSum == "bust":
            reward = -10
        elif dealerSum > 21:
            reward = 10
        elif agentSum == 21:
            reward = 30
        elif agentSum < dealerSum:
            reward = -10
        elif agentSum > dealerSum:
            reward = 10
        elif agentSum == dealerSum:
            reward = 0
            
        return reward
    
    def sumCards(hand, dealerHand): 
        #Returns sum of hand or bust
        sum = 0
        for x in range(len(hand)):
            if hand[x].rank == "J" or hand[x].rank == "Q" or hand[x].rank == "K":
                sum += 10
            elif hand[x].rank == "A":
                sum += 11
            else:
                sum += int(hand[x].rank, 10)
        if (sum > 21 and dealerHand == False):
            sum = "bust"
        return sum
    
    def getValue(card): 
        #Converts face cards and aces to numerical values
        if card.rank == "J" or card.rank == "Q" or card.rank == "K":
            return 10
        elif card.rank == "A":
            return 11
        else:
            return int(card.rank, 10)
        return 0
    
Agent.main()